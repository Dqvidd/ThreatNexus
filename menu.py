import questionary
from questionary import Style
from questionary import Separator
from termcolor import colored

def getMenu():
    """
    Function to obtain the menu of the actions to be performed.

    """

    try:
        custom_style_fancy = Style(
            [
                ("separator", "fg:#009975 bold"),
                ("qmark", "fg:#009975 bold"),
                ("question", "fg:#0000ff bold"),
                ("selected", "fg:#0000ff"),
                ("pointer", "fg:#0000ff bold"),
                ("highlighted", "fg:#0000ff bold"),
                ("answer", "fg:#0000ff bold"),
                ("text", "fg: #FFFFFF"),
            ]
        )

        choices = questionary.checkbox(
            "Welcome to ThreatNexus",
            choices=[
                Separator('==================================='),
                "IP Address",
                "Domain Name",
                "File Hash (MD5/SHA1/SHA256)",
                "Quit",
                Separator('==================================='),
                ],
            style=custom_style_fancy,
            qmark="[*]",
        ).ask()

        return choices
    
    except Exception as e:
        print(colored('There has been a problem with the program!','red'))
        exit(1)