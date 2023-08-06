# Copyright (C) 2019 Blu Wireless Ltd.
# All Rights Reserved.
#
# This file is part of BLADE.
#
# BLADE is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# BLADE is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# BLADE.  If not, see <https://www.gnu.org/licenses/>.
#

import argparse
from concurrent.futures import ThreadPoolExecutor
from fnmatch import fnmatch
import importlib
import json
import multiprocessing
import os
from pathlib import Path
import random
import sys
from time import sleep

from designformat import *

from .common.blob import load_and_classify
from .common.logging import (log_info, log_debug, log_warning, log_error,
                             set_verbosity, HIGH, LOW)
from .common.rules import (get_specific_rules, get_general_rules,
                           count_specific_rules, count_general_rules)
from .driver import do_generate
from .worker import worker

def main():
    """ Entrypoint for the templating engine """
    parser = argparse.ArgumentParser(
        description="Hierarchical templating tool for DesignFormat blobs"
    )

    # Setup arguments
    # - Input DF blob file (positional argument)
    parser.add_argument("input", help="Input DesignFormat blob file")
    # - Output directory for generated files
    parser.add_argument("output_dir", help="Output directory for generated files")
    # - Template directory
    parser.add_argument(
        "-t", "--templates", action="append", default=[], required=True,
        help="Provide a directory containing templates (searched recursively)"
    )
    # - Ruleset definition
    parser.add_argument(
        "-r", "--ruleset", action="append", default=[],
        help="Include a ruleset for controlling template generation"
    )
    # - Generation controls
    parser.add_argument(
        "-x", "--exclude", action="append", default=[],
        help="Exclude nodes that are present in another DesignFormat blob to "
             "avoid duplicate file generation"
    )
    parser.add_argument(
        "-s", "--skip", action="append", default=[],
        help="Skip the generation of files matching the provided pattern, for "
             "example --skip *.html"
    )
    parser.add_argument(
        "-p", "--parallel", default=5, type=int,
        help="Specify how many threads may be used during generation"
    )
    parser.add_argument(
        "-D", "--define", action="append", default=[],
        help="Define a value to pass into the template with an optional value, "
             "e.g. --define ENABLE_TEST --define MY_VAL=123"
    )
    parser.add_argument(
        "-d", "--dependency", default=False,
        help="Location to write out Make-compatible dependency file"
    )
    parser.add_argument(
        "--dependency-target", default=False,
        help="Target to list dependencies against"
    )
    # - Miscellaneous
    parser.add_argument(
        "-o", "--other", action="append", default=[],
        help="Provide a path to a file that a template needs during render, for "
             "example a Verilog module that is being wrapped."
    )
    # - Verbosity controls
    parser.add_argument(
        "-q", "--quiet", action="store_true", default=False,
        help="Suppress INFO level messages from the generator"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", default=False,
        help="Enable DEBUG level messages from the generator"
    )

    # Evaluate arguments
    args = parser.parse_args()

    # If dependency file exists, remove it
    if args.dependency and os.path.exists(args.dependency):
        log_debug(f"Removing existing dependency file {args.dependency}")
        os.remove(args.dependency)

    # Setup verbosity
    if args.quiet: set_verbosity(LOW)
    if args.verbose: set_verbosity(HIGH)

    # Check parallelism
    if args.parallel <= 0:
        log_warning("No parallel jobs allowed for generation")

    # Check the input path exists
    if not os.path.exists(args.input) or not os.path.isfile(args.input):
        log_error(f"Cannot open DesignFormat blob at path: {args.input}")
        sys.exit(1)

    # Load and classify the main DesignFormat blob
    log_debug("Loading main blob file")
    df_root, classified = load_and_classify(args.input)

    # For every exclude, load and classify the blob and build list of exclusions
    log_debug("Iterating through exclusion blobs:")
    exclusions = {}
    for exclude in args.exclude:
        # Skip the input blob if it is referenced
        if os.path.abspath(args.input) == os.path.abspath(exclude):
            log_warning(f" - Skipping {exclude} as it is the same as the input file")
            continue
        # Load the exclusion file
        log_debug(f" - Exclude: {exclude}")
        _, excludes = load_and_classify(exclude)
        # Work through node types
        for node_type in excludes:
            if node_type not in exclusions: exclusions[node_type] = []
            if node_type == DFBlock:
                exclusions[node_type] += [x.type for x in excludes[node_type]]
            else:
                exclusions[node_type] += [x.id for x in excludes[node_type]]

    # Apply the exclusions
    log_debug("Applying exclusions:")
    for node_type in classified:
        # If we don't have any exclusions for this type, skip
        if not node_type in exclusions: continue
        log_debug(f" - Running exclusions for {node_type.__name__}")
        # For DFBlock, filter by 'type'
        if node_type == DFBlock:
            log_debug("   * Before exclusions  : " + ', '.join([x.type for x in classified[node_type]]))
            log_debug("   * Applying exclusions: " + ', '.join([x for x in exclusions[node_type]]))
            classified[node_type] = [
                x for x in classified[node_type] if x.type not in exclusions[node_type]
            ]
            log_debug("   * After exclusions   : " + ', '.join([x.type for x in classified[node_type]]))
        # For everything else, filter by 'id'
        else:
            log_debug("    * Before exclusions  : " + ', '.join([x.id for x in classified[node_type]]))
            log_debug("    * Applying exclusions: " + ', '.join([x for x in exclusions[node_type]]))
            classified[node_type] = [
                x for x in classified[node_type] if x.id not in exclusions[node_type]
            ]
            log_debug("    * After exclusions   : " + ', '.join([x.id for x in classified[node_type]]))

    # Register every ruleset
    log_debug("Starting to register rules")
    for path in args.ruleset:
        # Check for the ruleset
        if not os.path.exists(path) or not os.path.isfile(path):
            log_error(f"Ruleset provided at path {path} is not a file")
            sys.exit(1)
        # Append the parent directory to the search path
        sys.path.append(os.path.dirname(os.path.abspath(path)))
        # Perform the import
        before = count_specific_rules() + count_general_rules()
        log_debug(f" - Loading rules from {path}")
        exec(f"import {os.path.splitext(os.path.basename(path))[0]} as _")
        after  = count_specific_rules() + count_general_rules()
        log_debug(f" - Registered {after-before} rules from {path}")
    log_debug(f"Registered a total of {count_specific_rules() + count_general_rules()} rules")

    # Compile defined values
    log_debug("Building map of defined values")
    defines = {}
    for define in args.define:
        if '=' in define:
            parts = define.split('=')
            defines[parts[0].strip()] = parts[1].strip()
        else:
            defines[define.strip()] = True

    # Create a lookup of every available template
    templates     = {}
    template_dirs = []
    log_debug(f"Searching for templates in directories provided")
    for t_dir in args.templates:
        start_count = len(templates.keys())
        template_dirs.append(t_dir)
        # Check for the directory
        if not os.path.exists(t_dir) or not os.path.isdir(t_dir):
            log_error(f"Template directory {t_dir} does not exist")
            sys.exit(1)
        # Identify all templates in this directory
        for template in Path(t_dir).rglob('*'):
            # Keep track of directories
            if template.is_dir():
                template_dirs.append(template.as_posix())
                continue
            # Ignore anything that is not a file
            elif not template.is_file():
                continue
            # Register the template
            templates[template.name] = template.absolute()
        log_debug(f" - Found {len(templates.keys())-start_count} templates under {t_dir}")
    log_debug(f"Found a total of {len(templates.keys())} templates")

    # Setup a routine for checking matches
    def check_match(expected, node_check, node_lookup):
        matched = True
        for key in expected:
            exp_val  = expected[key]
            # If the attribute doesn't exist then check if expectation was False
            if not node_check(key):
                if not exp_val: continue
                matched = False
                break
            node_val = node_lookup(key)
            # For boolean values, check for an exact match
            if isinstance(node_val, bool):
                if isinstance(exp_val, bool) and node_val == exp_val:
                    continue
                elif exp_val == '*':
                    continue
                matched = False
                break
            # For string values, check for a wildcard match
            elif isinstance(exp_val, str) and isinstance(node_val, str) and not fnmatch(node_val, exp_val):
                matched = False
                break
            # If a wildcard is given, allow any value
            elif exp_val == '*' and not node_val:
                matched = False
                break
            # If 'None' is specified, only allow a false value
            elif exp_val == None and node_val:
                matched = False
                break
        return matched

    # Run through the nodes, applying whatever specific rules are valid
    log_debug("Working through specific rules to build generation tasks")
    tasks     = []
    filenames = {}
    for node_type in classified:
        log_debug(f" - Iterating through nodes of type {node_type.__name__}")
        for node in classified[node_type]:
            log_debug(f"   + Iterating through specific rules for {node_type.__name__}::{node.id}")
            for rule in get_specific_rules():
                # Check the rule applies to this node type
                if not isinstance(node, rule.type): continue
                # Check that the environment attributes match up
                def check_env(key): return (key in os.environ)
                def get_env(key): return os.environ[key]
                if not check_match(rule.env, check_env, get_env): continue
                # Check that the attributes match up
                if not check_match(rule.attrs, node.getAttribute, node.getAttribute): continue
                # Check that the properties match up
                def check_prop(key): return hasattr(node, key)
                def get_prop(key): return getattr(node, key)
                if not check_match(rule.props, check_prop, get_prop): continue
                # Apply the rule
                log_debug(f"     * Applying specific rule {rule.func.__name__} to {node_type.__name__}::{node.id}")
                for task in rule.func(node, df_root): # Expects rule to be a generator
                    task.set_output_path(os.path.abspath(os.path.join(
                        args.output_dir, task.filename.strip()
                    )))
                    task.set_template_path(task.resolve_template(node, templates))
                    skips = [fnmatch(task.filename, x) for x in args.skip]
                    if True in skips:
                        log_debug(f"   + Skipping {task.filename} generation")
                    elif task.filename in filenames:
                        log_error(
                            f"Rule {rule.func.__name__} tried to create duplicate "
                            f"file {task.filename} from {node_type.__name__}::"
                            f"{node.id} - original created by {filenames[task.filename]}"
                        )
                        sys.exit(1)
                    elif not task.template_path:
                        log_error(
                            f"Rule {rule.func.__name__} tried to request an unknown "
                            f"template {task.template} from {node_type.__name__}::"
                            f"{node.id}"
                        )
                        sys.exit(1)
                    else:
                        tasks.append(task)
                        filenames[task.filename] = rule.func.__name__
    log_debug(f"Completed specific rule evaluation, created {len(tasks)} tasks")

    # Run through the general rules, providing them with all matching nodes
    log_debug("Working through general rules to build generation tasks")
    for rule in get_general_rules():
        log_debug(f" - Finding nodes matching general rule {rule.func.__name__}")
        candidates = []
        # If DFBase is specified, then all node types should be included
        if rule.type == DFBase:
            log_debug("   + Rule specifies type as DFBase, including all nodes")
            for node_type in classified.keys():
                candidates += classified[node_type]
        # Otherwise just include the correct classification result
        else:
            log_debug(f"   + Rule specifies type as {rule.type.__name__}")
            candidates = classified[rule.type] if rule.type in classified else []
        # If no candidates identified, move on
        if len(candidates) == 0: continue
        # Build a list of matches
        matches = []
        for node in candidates:
            log_debug(f"   + Checking if {type(node).__name__}::{node.id} matches")
            # Check that the environment attributes match up
            def check_env(key): return (key in os.environ)
            def get_env(key): return os.environ[key]
            if not check_match(rule.env, check_env, get_env): continue
            # Check that the attributes match up
            if not check_match(rule.attrs, node.getAttribute, node.getAttribute): continue
            # Check that the properties match up
            def check_prop(key): return hasattr(node, key)
            def get_prop(key): return getattr(node, key)
            if not check_match(rule.props, check_prop, get_prop): continue
            # Rule matches this node, so include it
            log_debug(f"     * Rule matches node {type(node).__name__}::{node.id}")
            matches.append(node)
        # Apply the rule
        log_debug(f"   + Applying general rule {rule.func.__name__} to {len(matches)} nodes")
        for task in rule.func(matches, df_root):
            task.set_output_path(os.path.abspath(os.path.join(
                args.output_dir, task.filename.strip()
            )))
            task.set_template_path(task.resolve_template(matches[0], templates))
            skips = [fnmatch(task.filename, x) for x in args.skip]
            if True in skips:
                log_debug(f"   + Skipping {task.filename} generation")
            elif task.filename in filenames:
                log_error(
                    f"Rule {rule.func.__name__} tried to create duplicate "
                    f"file {task.filename} original created by " +
                    filenames[task.filename]
                )
                sys.exit(1)
            elif not task.template_path:
                log_error(
                    f"Rule {rule.func.__name__} tried to request an unknown "
                    f"template {task.template}"
                )
                sys.exit(1)
            else:
                tasks.append(task)
                filenames[task.filename] = rule.func.__name__

    log_debug(f"Completed general rule evaluation, now have {len(tasks)} tasks")

    # Eliminate any generation where the inputs are not updated
    latest_blob = os.path.getmtime(args.input)
    for exclude in args.exclude:
        mtime = os.path.getmtime(exclude)
        if mtime > latest_blob: latest_blob = mtime

    for task in tasks[:]:
        # If the file doesn't exist, generate it
        if not os.path.exists(task.output_path): continue
        # Get the modification time of the template and file
        tmpl_mtime = os.path.getmtime(task.template_path)
        out_mtime  = os.path.getmtime(task.output_path)
        # If either blobs or template are newer, regenerate
        if tmpl_mtime > out_mtime or latest_blob > out_mtime: continue
        # Otherwise drop the task
        tasks.remove(task)

    # If parallelism is positive, use worker processes
    success   = True
    completed = {}

    def check_task(task):
        if task.succeeded:
            log_info(f"Generated {task.filename} from {task.template}")
        else:
            log_error(
                f"Failed to generate {task.filename} due to {len(task.errors)} "
                f"error(s)"
            )
            for error in task.errors:
                log_error(f" - {error}")
        if task.filename.strip() in completed:
            log_error(f"Already had completion for {task.filename.strip()}")
            sys.exit(1)
        completed[task.filename.strip()] = task
        return task.succeeded

    if args.parallel > 0:
        # Randomly allocate tasks across the workers
        worker_tasks = [[] for i in range(args.parallel)]
        while len(tasks) > 0:
            for i in range(args.parallel):
                if len(tasks) == 0: break
                task = random.choice(tasks)
                worker_tasks[i].append(task)
                tasks.remove(task)

        # Create a queue for each worker to return task status
        worker_qs = [multiprocessing.Queue() for i in range(args.parallel)]

        # Dispatch a worker for each task set
        worker_ps = []
        for idx, tasks in zip(range(args.parallel), worker_tasks):
            p = multiprocessing.Process(target=worker, args=(
                args.input, tasks, template_dirs, templates, args.output_dir,
                defines, args.other, worker_qs[idx]
            ))
            p.start()
            worker_ps.append(p)

        # Wait for all tasks to complete
        log_debug(f"Waiting for {len(worker_ps)} worker processes to complete")
        while len(worker_ps) > 0:
            sleep(0.1)
            for i in range(len(worker_ps)):
                # Run through the return queue looking for task success/failure
                while not worker_qs[i].empty():
                    success &= check_task(worker_qs[i].get())

                # Check if the process has now completed
                if not worker_ps[i].is_alive():
                    log_debug("Worker process has completed")
                    del worker_qs[i]
                    del worker_ps[i]
                    break

    # Otherwise execute all generation tasks natively
    else:
        for task in tasks:
            do_generate(
                task, task.lookup_nodes(classified), df_root, template_dirs,
                templates, args.output_dir, defines, args.other
            )
            success &= check_task(task)
            if not success:
                log_error(f"Generation of {task.filename} failed")
                sys.exit(1)

    log_debug("All generation tasks completed")

    # On success, write out a dependency file
    if success and args.dependency:
        log_debug(f"Creating dependency file {args.dependency}")
        deps  = [os.path.abspath(args.input)]
        deps += [os.path.abspath(x) for x in args.exclude]
        for task in completed.values():
            deps += [task.template_path, os.path.abspath(args.input)]
        deps += [os.path.abspath(x) for x in args.ruleset]
        # Uniquify dependencies
        deps = list(set(deps))
        # Write dependency file
        with open(args.dependency, 'w') as fh:
            target = args.dependency_target if args.dependency_target else args.dependency
            fh.write(f"{target}: " + ' '.join(deps) +"\n\n")

    # Exit with the success/failure
    if not success: log_error("Generation failed - see previous errors")
    sys.exit(0 if success else 1)

# Invoke main when executing this file
if __name__ == "__main__": main()
