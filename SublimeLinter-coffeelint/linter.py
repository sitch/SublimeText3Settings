#
# coffeelint.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Coffeelint plugin class."""

from SublimeLinter.lint import Linter, persist


class Coffeelint(Linter):

    """Provides an interface to coffeelint."""

    syntax = ('coffeescript', 'coffeescript_literate')
    executable = 'coffeelint'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.4.0'
    regex = (
        r'^<issue line="(?P<line>\d+)"\s*\r?\n'
        r'\s*lineEnd="\d+"\s*\r?\n'
        r'\s*reason="\[(?:(?P<error>error)|(?P<warning>warn))\]\s+'
        r'(?:\[stdin\]:\d+:(?P<col>\d+):\s+error:\s+)?'
        r'(?P<message>[^"\n\r]+)["\n\r]'
    )
    multiline = True
    comment_re = r'\s*#'
    config_file = ('-f', 'coffeelint.json', '~')

    def cmd(self):
        """Return a tuple with the command line to execute."""

        command = [self.executable_path, '--reporter', 'jslint', '--stdin']

        if persist.get_syntax(self.view) == 'coffeescript_literate':
            command.append('--literate')

        return command
