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

from hashlib import md5
import json
import os
import re
import sys
import time

from mako.lookup import TemplateLookup
from mako import exceptions

from designformat import DFProject, DFConstants, DFDefine, DFBlock, DFInterconnect
from designformat import DFRegisterGroup, DFCommand, DFPort

from .common.generation import GenTask
from .common.logging import log_debug, log_info, log_warning, log_error

def do_generate(
    task       : GenTask,
    nodes      : list,
    project    : DFProject,
    tmpl_dirs  : list,
    templates  : dict,
    target     : str,
    defines    : dict,
    other_paths: list,
):
    """
    Drive Mako templating engine to generate a file described by a generation
    task. Errors are written back to the task so that it can run under a thread
    pool executor.

    Args:
        task       : The generation task to perform
        nodes      : List of the DesignFormat nodes to process
        project    : DesignFormat DFProject containing this node
        tmpl_dirs  : All of the directories to add to the template lookup
        templates  : Map of all templates that are registered
        target     : Path to the output directory
        defines    : Extra values defined on the command line
        other_paths: Additional paths to files required by templates
    """
    # Get the full path to the template, node source, and output file
    template  = task.template.strip()
    node_path = nodes[0].getAttribute('source_path')

    # Check if template exists
    if not task.template_path:
        task.add_error(f"Could not find template {task.template}")
        return

    # Build the context for the template file
    source_time = time.ctime(os.path.getmtime(node_path)) if node_path and os.path.exists(node_path) else None
    blade_ctx = {
        # Expose the externally provided defines
        "ext_defines"   : defines,
        # Fields relating to the files being used to generate output
        "template_path" : task.template_path,
        "template_time" : time.ctime(os.path.getmtime(task.template_path)),
        "generator_path": sys.argv[0],
        "generator_time": time.ctime(os.path.getmtime(sys.argv[0])),
        "source_path"   : node_path,
        "source_time"   : source_time,
        "output_path"   : task.output_path,
        # Expose the DFProject
        "project"       : project,
        # Add 'None' for each principal node type by default
        "block"         : None,
        "interconnect"  : None,
        "reg_groups"    : [x for x in nodes if isinstance(x, DFRegisterGroup)],
        "commands"      : [x for x in nodes if isinstance(x, DFCommand)],
        "defines"       : [x for x in nodes if isinstance(x, DFDefine)],
        # Provide 'other' paths that templates may require
        "other"         : other_paths,
    }

    # Select a block to add to the context
    blocks = [x for x in nodes if isinstance(x, DFBlock)]
    if len(blocks) > 0:
        if len(blocks) > 1:
            log_warning(
                f"Multiple DFBlocks ({len(blocks)}) present, only using the first."
            )
        blade_ctx['block'] = blocks[0]

    # Select an interconnect to add to the context
    interconnects = [x for x in nodes if isinstance(x, DFInterconnect)]
    if len(interconnects) > 0:
        if len(interconnects) > 1:
            print(
                f"WARNING: Multiple DFInterconnect ({len(interconnects)}) present, "
                "only generating the first."
            )
        blade_ctx['interconnect'] = interconnects[0]

    # Merge in the command line defines (don't allow it to override scope vars)
    for key in defines:
        if not key in blade_ctx:
            blade_ctx[key] = defines[key]

    # Declare a function to check if a value has been defined
    def ifdef(key):
        return (key in defines)
    blade_ctx['ifdef'] = ifdef

    # Import all templates into the lookup
    # NOTE: We always drag in the BLADE Core and Templating so that we have
    #       access to common functions and templates (like the copyright)
    all_dirs = [
        *tmpl_dirs,
        os.path.abspath(os.path.dirname(__file__)),
        os.path.abspath(os.path.dirname(task.template_path)),
    ]

    # Add the template directories onto the path to support imports
    for t_dir in all_dirs: sys.path.append(t_dir)

    # Build the lookup
    lookup = TemplateLookup(
        directories = all_dirs,
        imports     = [
            "from datetime import datetime",
            "import math",
            "import os",
            "import re",
            "from designformat import DFBlock, DFCommand, DFConstants, DFDefine,"
            "DFInterconnect, DFPort, DFConstantTie, DFPort, DFConnection",
        ]
    )

    # Render the template
    rendered = None
    try:
        rendered = lookup.get_template(os.path.basename(task.template)).render(**blade_ctx)
    except Exception:
        task.add_error(
            "An exception was raised while rendering the template: " +
            exceptions.text_error_template().render()
        )
        return

    # Ensure output directory tree exists
    log_debug(f"Ensuring directory {os.path.dirname(task.output_path)} exists")
    os.makedirs(os.path.dirname(task.output_path), exist_ok=True)

    # Write the rendered output to file
    log_debug(f"Writing out {task.output_path}")
    with open(task.output_path, "w") as fh:
        fh.write('\n'.join([x.rstrip() for x in rendered.split('\n')]))