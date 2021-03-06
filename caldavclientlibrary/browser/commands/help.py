##
# Copyright (c) 2007-2016 Apple Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from caldavclientlibrary.browser.command import Command
from caldavclientlibrary.browser.command import WrongOptions
import getopt
import shlex


class Cmd(Command):

    def __init__(self):
        super(Command, self).__init__()
        self.cmds = ("help", "?",)

    def execute(self, cmdname, options):
        opts, args = getopt.getopt(shlex.split(options), '')
        if len(opts) or len(args) > 1:
            print self.usage(cmdname)
            raise WrongOptions()
        self.shell.help(cmd=(None if len(args) == 0 else args[0]))
        return True

    def usage(self, name):
        return """Usage: %s [CMD]
CMD is the name of a command.
""" % (name,)

    def hasHelp(self, name):
        return name in ("help",)

    def helpDescription(self):
        return "Displays help about a command."
