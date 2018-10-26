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
	|	* planets (get_details('planets'))
	|	|
	|	|	add_planet()
	|	|	add_connection()
	|	|
	|
	|	* players (get_details('players'))
	|	|
	|	|	add_player()
	|	|	materialize_resources()
	|	|	banish_resources()
	|	|	transfer_resources()
	|	|
	|	
	|	* ships (get_details('ships'))
	|	|
	|	|	register_ship()
	|	|	materialize_ship()
	|	|	banish_ship()
	|	|	make_ship()
	|	|	scrap_ship()
	|	|
	|	|	* fleets (potentially extend get_details() to fleets?)
	|	|	|
	|	|	|	make_fleet()
	|	|	|	disband_fleet()
	|	|	|	hohman_transfer()
	|	|	|	brachistochrone_transfer()
	|	|	|
	|	|
	|		

get_details() is called at every indicated submenu.
All menus and submenus will have a back button!
