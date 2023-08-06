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

import os

import designformat
from designformat import DFBlock

# ==============================================================================
# Generation
# ==============================================================================

class GenTask(object):

    def __init__(self, nodes, template, filename, parameters):
        node_list = nodes if isinstance(nodes, list) else [nodes]
        self.__nodes = []
        for node in node_list:
            if isinstance(node, DFBlock):
                self.__nodes.append(f"DFBlock::{node.type}")
            else:
                self.__nodes.append(f"{type(node).__name__}::{node.id}")
        self.__template      = template
        self.__filename      = filename
        self.__parameters    = parameters
        # Output variables
        self.__errors        = []
        self.__output_path   = None
        self.__template_path = None

    @property
    def nodes(self): return self.__nodes

    @property
    def template(self): return self.__template.strip()

    @property
    def filename(self): return self.__filename

    @property
    def parameters(self): return self.__parameters

    def add_error(self, message): self.__errors.append(message)

    @property
    def errors(self): return self.__errors[:]

    @property
    def succeeded(self): return len(self.__errors) == 0

    def set_output_path(self, path): self.__output_path = path

    @property
    def output_path(self): return self.__output_path

    def set_template_path(self, path): self.__template_path = path

    @property
    def template_path(self): return self.__template_path

    def lookup_nodes(self, classified):
        real = []
        for node in self.nodes:
            n_parts = node.split('::')
            n_type  = designformat.__dict__[n_parts[0].strip()]
            n_id    = n_parts[1].strip()
            if n_type == DFBlock:
                found = [x for x in classified[n_type] if x.type == n_id]
                real.append(found[0])
            else:
                found = [x for x in classified[n_type] if x.id == n_id]
                real.append(found[0])
        return real

    def resolve_template(self, node, templates):
        if self.template in templates:
            return templates[self.template].as_posix()
        elif self.template.startswith('/') and os.path.exists(template):
            return template
        elif node.getAttribute('source_path'):
            path = os.path.abspath(os.path.join(
                os.path.dirname(node.getAttribute('source_path')),
                self.template
            ))
            if os.path.exists(path): return path
        return None

def generate(node, template, filename, parameters={}):
    """ Register a file that should be generated.

    Args:
        node      : One or a list of DesignFormat nodes to work with
        template  : The absolute path or localised reference to a template
        filename  : The output filename to generate
        parameters: Optional, additional parameters to pass into generation
    """
    return GenTask(node, template, filename, parameters)
