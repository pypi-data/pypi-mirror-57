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

# ==============================================================================
# Logging
# ==============================================================================

# Declare a colour chart (bash colour codes)
colours = {
    "red": 31, "green": 32, "yellow": 33, "blue": 34, "purple": 35, "cyan": 36,
}

# Declare verbosities
LOW       = 0
MEDIUM    = 1
HIGH      = 2
curr_verb = MEDIUM

# Declare a mapping between priority and colour
colour_map = {
    "WARNING": colours["yellow"],
    "ERROR"  : colours["red"],
    "INFO"   : colours["blue"],
    "DEBUG"  : colours["cyan"],
}

# Specify what messages should be seen at each verbosity level
verbosity_map = {
    LOW   : ["ERROR", "WARNING"],
    MEDIUM: ["ERROR", "WARNING", "INFO"],
    HIGH  : ["ERROR", "WARNING", "INFO", "DEBUG"],
}

def set_verbosity(verbosity):
    """ Change the verbosity level

    Args:
        verbosity: The verbosity level to set
    """
    global curr_verb
    assert verbosity >= LOW and verbosity <= HIGH
    curr_verb = verbosity

def log_message(priority, message):
    """ Print out a log message with the correct formatting

    Args:
        priority: The level (debug/info/warning/error) to print at
        path    : Hierarchical path of object being printed
        message : Message to print
    """
    # Check if the verbosity is sufficient to print this message
    if priority not in verbosity_map[curr_verb]: return
    # Format and print (checking if terminal supports colouration)
    log_msg = f"[{priority}] "
    log_msg += message
    if priority in colour_map and 'TERM' in os.environ and 'xterm' in os.environ['TERM']:
        print(f"\033[1;{colour_map[priority]}m{log_msg}\033[0m")
    else:
        print(log_msg)

def log_debug(message): log_message("DEBUG", message)
def log_info(message): log_message("INFO", message)
def log_warning(message): log_message("WARNING", message)
def log_error(message): log_message("ERROR", message)