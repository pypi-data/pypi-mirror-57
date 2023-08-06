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

from designformat import DFBase

# ==============================================================================
# Rule Registration
# ==============================================================================

# Ruleset that generate files specific to a node
specific_ruleset = []

# Ruleset that generates files encompassing all matching nodes
general_ruleset  = []

class RuleEntry(object):

    def __init__(self, func, type, props, attrs, env):
        self.__func  = func
        self.__type  = type
        self.__props = props
        self.__attrs = attrs
        self.__env   = env

    @property
    def func(self): return self.__func

    @property
    def type(self): return self.__type

    @property
    def props(self): return self.__props

    @property
    def attrs(self): return self.__attrs

    @property
    def env(self): return self.__env

def rule(specific=True, type=DFBase, props={}, attrs={}, env={}):
    """ Decorator function for registering a rule

    Args:
        specific: Whether this rule takes a single node or multiple nodes
        type    : A DesignFormat node type to filter rules by
        props   : A map of properties to match
        attrs   : A map of attributes to match
        env     : A map of environment attributes to match
    """
    def wrap(f):
        rule = RuleEntry(f, type, props, attrs, env)
        (specific_ruleset if specific else general_ruleset).append(rule)
        return f
    return wrap

def get_specific_rules():
    """ Return all of the registered specific rules """
    return specific_ruleset[:]

def count_specific_rules():
    """ Return the number of registered specific rules """
    return len(specific_ruleset)

def get_general_rules():
    """ Return all of the registered general rules """
    return general_ruleset[:]

def count_general_rules():
    """ Return the number of registered general rules """
    return len(general_ruleset)