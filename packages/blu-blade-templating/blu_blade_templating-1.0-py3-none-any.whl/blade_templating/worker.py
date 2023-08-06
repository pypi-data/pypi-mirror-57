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

from multiprocessing import Queue

from .common.blob import load_and_classify
from .common.logging import log_debug as _log_debug
from .common.logging import log_info as _log_info
from .common.logging import log_warning as _log_warning
from .common.logging import log_error as _log_error
from .driver import do_generate
from designformat import *
import designformat

def log_debug(message): _log_debug(f"[WORKER] {message}")
def log_info(message): _log_info(f"[WORKER] {message}")
def log_warning(message): _log_warning(f"[WORKER] {message}")
def log_error(message): _log_error(f"[WORKER] {message}")

def worker(
    path       : str,
    tasks      : list,
    tmpl_dirs  : list,
    templates  : dict,
    target     : str,
    defines    : dict,
    other_paths: list,
    return_q   : Queue
):
    """
    Templating worker process that can be launched via multiprocessing.

    Args:
        path       : Path to the DesignFormat blob to load.
        task       : List of GenTasks for this worker to perform.
        tmpl_dirs  : All of the directories to add to the template lookup
        templates  : Map of all templates that are registered
        target     : Path to the output directory
        defines    : Extra values defined on the command line
        other_paths: Additional paths to files required by templates
        return_q   : Cross-process queue for returning failures
    """

    # Load the worker's copy of the blob file
    log_debug("Loading blob from: " + path)
    df_root, classified = load_and_classify(path)

    # Work through the rendering tasks
    log_debug(f"Starting to render {len(tasks)} tasks")
    for task in tasks:
        # First find all of the referenced nodes
        log_debug(f"Identifying {len(task.nodes)} nodes from the GenTask")
        nodes = task.lookup_nodes(classified)
        # Kick off the generation task
        log_debug(f"Kicking off the generation task")
        do_generate(
            task, nodes, df_root, tmpl_dirs, templates, target, defines,
            other_paths
        )
        # Queue the task back to the master (returns errors etc)
        return_q.put(task)
    log_debug(f"All tasks completed")

