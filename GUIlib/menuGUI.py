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
import PyQt5

class ObjectGUI(MenuGUI):
    """
    Main GUI Object.

    Work in progress!
    """

    # Classwide variables.
    campaign_title = "Incursion Campaign"

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

        # Initalizing GUI!
        self.initGUI()

    def initGUI(self):
        """
        Initalizes GUI with inital class parameters.
        """
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title())

# In case the user runs this library:
if __name__ == '__main__':
    # Accepts command line arguments.
    myGUI = ObjectGUI()
    print("You've run the GUI Library " + sys.argv[0] + "with arguments: " + str(sys.argv))
