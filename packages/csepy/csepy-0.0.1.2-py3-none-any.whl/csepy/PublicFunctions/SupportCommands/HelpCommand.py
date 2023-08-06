#!/usr/bin/python3
from csepy.PublicFunctions.CommandInterface.ICommand import ICommand
from csepy.System.EndpointMap.EndpointMapper import CommandMapping


class HelpCommand(ICommand):
    def Execute(self):
        helpText = "\n".join(["\t\t{0:30}{1}".format(command, CommandMapping[command].ShortHelp)
                              for command in CommandMapping if command != "help"
                              and hasattr(CommandMapping[command], "ShortHelp")])
        helpText = f"Public functions available. for more information type " \
                   f"--help after the desired function\n{helpText}"
        self.context.Logger.INFO(helpText)


HelpCommand.PublicFacing = "help"
HelpCommand.Help = "Lists all public facing commands in service with short descriptions for each command"
