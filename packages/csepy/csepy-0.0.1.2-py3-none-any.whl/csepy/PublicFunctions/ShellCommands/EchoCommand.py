#!/usr/bin/python3
from csepy.PublicFunctions.CommandInterface.ICommand import ICommand


class EchoCommand(ICommand):
    def Execute(self):
        self.RunShellCommand(f"echo {' '.join(self.request)}")


EchoCommand.PublicFacing = "echo"
EchoCommand.MinRequestParameters = 1
EchoCommand.Help = "Repeats any parameters passed\n" \
                   "echo [text]\n" \
                   "text- the text that will be printed in the console window, " \
                   "does not need to be encapsulated in quotes"
EchoCommand.ShortHelp = "Repeats any parameters passed"
