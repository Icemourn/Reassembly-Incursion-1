------------------------------------------------------------------------
GUI Library Readme
GUI Planning & Notes

Authors: Icemourn

Last updated: ................................................ 26 Oct 18
------------------------------------------------------------------------

Currently planning GUI:

Flowchart (V 0.1):

	* Main menu
	|
	|	>>> INITALIZATION & SAVE FILE DETECTION <<<
	|
	|	exit()
	|	end_turn()
	|	start_turn()
	|
	|	* Planets (get_details('planets'))
	|	|
	|	|	add_planet()
	|	|	add_connection()
	|	|
	|
	|	* Players (get_details('players'))
	|	|
	|	|	add_player()
	|	|	materialize_resources()
	|	|	banish_resources()
	|	|	transfer_resources()
	|	|
	|	
	|	* Ships (get_details('ships'))
	|	|
	|	|	register_ship()
	|	|	materialize_ship()
	|	|	banish_ship()
	|	|	make_ship()
	|	|	scrap_ship()
	|	|
	|	|	* Fleets (potentially extend get_details() to fleets?)
	|	|	|
	|	|	|	make_fleet()
	|	|	|	disband_fleet()
	|	|	|	hohman_transfer()
	|	|	|	brachistochrone_transfer()
	|	|	|
	|	|
	|		

Development notes:

get_details() is called at every indicated submenu.
All menus and submenus will have a back button!

I currently plan to make the GUI a state machine.
Planned GUI states are:

	MainMenu
	Planets
	Players
	Ships
	Fleets

State machine flow will be same as the flowchart above.
