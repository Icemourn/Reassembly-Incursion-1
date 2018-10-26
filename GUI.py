from CampaignCommands import Commands
from IncursionInit import initalizeSave

from GUIlib.menuGUI import ObjectGUI

from os import listdir

if __name__ == '__main__':
    # Accepts command line arguments.
    myGUI = ObjectGUI()
    print("You've run the GUI Exceutable " + sys.argv[0] + "with arguments: " + str(sys.argv))
