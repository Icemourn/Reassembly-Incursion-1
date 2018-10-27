# ----------------------------------------------------------------------
# Incursion Campaign Window-Based GUI
# User-friendliness!
#
# Authors: Icemourn
#
# Last updated: .............................................. 26 Oct 18
# ----------------------------------------------------------------------

"""
The idea is to create a windowed GUI with buttons and text boxes to
improve the user friendliness of the underlying commands.

~Icemourn
"""

from sys import argv
from enum import Enum
import PyQt5

class ObjectGUI(MenuGUI):
    """
    Main GUI Object.

    Work in progress!
    """

    # Classwide variables.
    campaign_title = "Incursion Campaign"

    # Internal Enumerator class for state control.
    class stateEnum(Enum):
        """
        State enumerator for GUI menus.
        """
        # Note: states are in camel case.
        Null = 0
        MainMenu = 1
        Planets = 2
        Players = 3
        Ships = 4
        Fleets = 5

    # Classwide methods:
    def __init__(self):
        """
        GUI Object constructor.
        """

        # Obligatory superclass initalization... for some reason.
        super.__init__()

        # Window parameters:
        self.title = campaign_title + "GUI"
        self.left = 60
        self.top = 60
        self.height = 640
        self.width = 480

        # Finite-state machine parameter:
        self.state = stateEnum.Null

        # Initalizing GUI!
        self.initGUI()

    def initGUI(self):
        """
        Initalizes GUI with inital class parameters and sets state to
        "MainMenu".
        """
        # Window parameters
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title())

        # State parameter
        self.state = stateEnum.MainMenu

# In case the user runs this library:
if __name__ == '__main__':
    # Accepts command line arguments.
    myGUI = ObjectGUI()
    print("You've run the GUI Library " + sys.argv[0] + "with arguments: " + str(sys.argv))
