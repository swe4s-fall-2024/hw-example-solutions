"""
This module provides custom formatting for command-line argument parsing using the argparse module.
"""

import argparse

class ArgsFormatter(argparse.HelpFormatter):
    """
    Custom argument formatter for argparse that overrides the default formatting 
    of action invocations, removing extra spaces between option flags and displaying 
    them in a cleaner format.

    Methods:
        _format_action_invocation(action):
            Overrides the default method in argparse.HelpFormatter to customize 
            how the action's option strings are displayed in the help message.
    """

    def _format_action_invocation(self, action):
        """
        Customizes the formatting of action invocations (i.e., how options are 
        displayed in the help message).

        Args:
            action (argparse.Action): The action associated with a command-line option.
        
        Returns:
            str: A string representing the option strings (e.g., '-h, --help') 
                 joined by a comma without extra spaces.
        """
        if not action.option_strings:
            return super()._format_action_invocation(action)

        parts = []
        for option_string in action.option_strings:
            parts.append(option_string)
        return ', '.join(parts)