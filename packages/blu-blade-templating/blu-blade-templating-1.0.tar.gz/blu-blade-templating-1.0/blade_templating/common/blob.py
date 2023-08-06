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

import json
import sys

from designformat import *
from .logging import log_error, log_debug

# ==============================================================================
# Blob Loading
# ==============================================================================

def load_and_classify(path : str):
    """ Load nodes from a DesignFormat blob and classify them into types.

    Args:
        path: Path to the DesignFormat blob

    Returns: Tuple of the project and the classified blobs
    """
    # Load the DesignFormat blob
    df_root = None
    try:
        log_debug(f"Loading DesignFormat blob from file {path}")
        with open(path, 'r') as fh:
            raw = json.load(fh)
            # If blob is empty, fail out
            if len(raw.keys()) == 0:
                log_error(f"DesignFormat blob {path} is empty")
                sys.exit(1)
            # Attempt to load the object
            df_root = DFProject().loadObject(raw)
            # Check for nodes
            if len(df_root.nodes.values()) == 0:
                log_error(f"DesignFormat blob {path} contains no nodes")
                sys.exit(1)
    except Exception as e:
        log_error(f"Failed to load DesignFormat blob {path}: {e}")
        sys.exit(1)

    # Separate out DesignFormat nodes into their different classes
    classified = {}
    # - First run through the top-level nodes
    for node in df_root.nodes.values():
        if not type(node) in classified:
            classified[type(node)] = []
        classified[type(node)].append(node)
    # - Now for any DFBlock nodes, chase the hierarchy
    def chase(block):
        # Check if this block is registered
        if not block in classified[DFBlock]: classified[DFBlock].append(block)
        # Chase through all children
        for child in block.children: chase(child)
    if DFBlock in classified:
        for block in classified[DFBlock]:
            chase(block)
    # - Log what we've found
    for key in classified:
        log_debug(
            f"Identified {len(classified[key])} nodes of type {key.__name__}: "
            f"{', '.join([x.id for x in classified[key]])}"
        )
    # - For DFBlock classification, uniquify by block type
    if DFBlock in classified:
        unique = []
        for block in classified[DFBlock]:
            if not block.type in [x.type for x in unique]:
                unique.append(block)
        log_debug(
            f"Identified {len(unique)} unique DFBlock types: " +
            ', '.join([x.type for x in unique])
        )
        classified[DFBlock] = unique
    # - For everything else, uniquify by ID
    for node_type in classified:
        if node_type == DFBlock: continue
        unique = []
        for node in classified[node_type]:
            if not node.id in [x.id for x in unique]:
                unique.append(node)
        log_debug(
            f"Identified {len(unique)} unique {node_type.__name__} types: " +
            ', '.join([x.id for x in unique])
        )
        classified[node_type] = unique

    # Return tuple
    return (df_root, classified)