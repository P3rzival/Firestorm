# Name: Conway's game of life
# Dimensions: 2

# --- Set up executable path, do not edit ---
import sys
import inspect
import logging
import random
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
this_file_loc = (inspect.stack()[0][1])
main_dir_loc = this_file_loc[:this_file_loc.index('ca_descriptions')]
sys.path.append(main_dir_loc)
sys.path.append(main_dir_loc + 'capyle')
sys.path.append(main_dir_loc + 'capyle/ca')
sys.path.append(main_dir_loc + 'capyle/guicomponents')
# ---

from capyle.ca import Grid2D, Neighbourhood, CAConfig, randomise2d
import capyle.utils as utils
import numpy as np

def wind(wind_direction, numValues, neighbourstates, grid):
    # adding up depending on wind and neighboar
    wind_north_n_north = (wind_direction == 'N') & (neighbourstates[1] == 5) & (grid != 5)
    wind_north_n_east = (wind_direction == 'N') & (neighbourstates[4] == 5) & (grid != 5)
    wind_north_n_west = (wind_direction == 'N') & (neighbourstates[3] == 5) & (grid != 5)
    wind_north_n_south = (wind_direction == 'N') & (neighbourstates[6] == 5) & (grid != 5)
    wind_north_n_north_east = (wind_direction == 'N') & (neighbourstates[2] == 5) & (grid != 5)
    wind_north_n_north_west = (wind_direction == 'N') & (neighbourstates[0] == 5) & (grid != 5)
    wind_north_n_south_east = (wind_direction == 'N') & (neighbourstates[7] == 5) & (grid != 5)
    wind_north_n_south_west = (wind_direction == 'N') & (neighbourstates[5] == 5) & (grid != 5)

    wind_east_n_north = (wind_direction == 'E') & (neighbourstates[1] == 5) & (grid != 5)
    wind_east_n_east = (wind_direction == 'E') & (neighbourstates[4] == 5) & (grid != 5)
    wind_east_n_west = (wind_direction == 'E') & (neighbourstates[3] == 5) & (grid != 5)
    wind_east_n_south = (wind_direction == 'E') & (neighbourstates[6] == 5) & (grid != 5)
    wind_east_n_north_east = (wind_direction == 'E') & (neighbourstates[2] == 5) & (grid != 5)
    wind_east_n_north_west = (wind_direction == 'E') & (neighbourstates[0] == 5) & (grid != 5)
    wind_east_n_south_east = (wind_direction == 'E') & (neighbourstates[7] == 5) & (grid != 5)
    wind_east_n_south_west = (wind_direction == 'E') & (neighbourstates[5] == 5) & (grid != 5)

    wind_west_n_north = (wind_direction == 'W') & (neighbourstates[1] == 5) & (grid != 5)
    wind_west_n_east = (wind_direction == 'W') & (neighbourstates[4] == 5) & (grid != 5)
    wind_west_n_west = (wind_direction == 'W') & (neighbourstates[3] == 5) & (grid != 5)
    wind_west_n_south = (wind_direction == 'W') & (neighbourstates[6] == 5) & (grid != 5)
    wind_west_n_north_east = (wind_direction == 'W') & (neighbourstates[2] == 5) & (grid != 5)
    wind_west_n_north_west = (wind_direction == 'W') & (neighbourstates[0] == 5) & (grid != 5)
    wind_west_n_south_east = (wind_direction == 'W') & (neighbourstates[7] == 5) & (grid != 5)
    wind_west_n_south_west = (wind_direction == 'W') & (neighbourstates[5] == 5) & (grid != 5)

    wind_south_n_north = (wind_direction == 'S') & (neighbourstates[1] == 5) & (grid != 5)
    wind_south_n_east = (wind_direction == 'S') & (neighbourstates[4] == 5) & (grid != 5)
    wind_south_n_west = (wind_direction == 'S') & (neighbourstates[3] == 5) & (grid != 5)
    wind_south_n_south = (wind_direction == 'S') & (neighbourstates[6] == 5) & (grid != 5)
    wind_south_n_north_east = (wind_direction == 'S') & (neighbourstates[2] == 5) & (grid != 5)
    wind_south_n_north_west = (wind_direction == 'S') & (neighbourstates[0] == 5) & (grid != 5)
    wind_south_n_south_east = (wind_direction == 'S') & (neighbourstates[7] == 5) & (grid != 5)
    wind_south_n_south_west = (wind_direction == 'S') & (neighbourstates[5] == 5) & (grid != 5)


    #Probability of ignition algorithm
    dir_wind_random = np.random.uniform(0.1, 0.15, (100,100))
    non_dir_wind_random = np.random.uniform(-0.05, -0.01, (100,100))
    side_wind_random = np.random.uniform(0.02, 0.06, (100,100))
    dir_side_wind_random = np.random.uniform(0.05, 0.08, (100,100))
    non_dir_side_wind_random = np.random.uniform(-0.03, 0.01, (100,100))
	
    numValues[wind_north_n_north]      += dir_wind_random[wind_north_n_north]
    numValues[wind_north_n_east]       += side_wind_random[wind_north_n_east]
    numValues[wind_north_n_west]       += side_wind_random[wind_north_n_west]
    numValues[wind_north_n_south]      += non_dir_wind_random[wind_north_n_south]
    numValues[wind_north_n_north_east] += dir_side_wind_random[wind_north_n_north_east]
    numValues[wind_north_n_north_west] += dir_side_wind_random[wind_north_n_north_west]
    numValues[wind_north_n_south_east] += non_dir_side_wind_random[wind_north_n_south_east]
    numValues[wind_north_n_south_west] += non_dir_side_wind_random[wind_north_n_south_west]

    numValues[wind_east_n_north]      += side_wind_random[wind_east_n_north]
    numValues[wind_east_n_east]       += dir_wind_random[wind_east_n_east]
    numValues[wind_east_n_west]       += non_dir_wind_random[wind_east_n_west]
    numValues[wind_east_n_south]      += side_wind_random[wind_east_n_south]
    numValues[wind_east_n_north_east] += dir_side_wind_random[wind_east_n_north_east]
    numValues[wind_east_n_north_west] += non_dir_side_wind_random[wind_east_n_north_west]
    numValues[wind_east_n_south_east] += dir_side_wind_random[wind_east_n_south_east]
    numValues[wind_east_n_south_west] += non_dir_side_wind_random[wind_east_n_south_west]

    numValues[wind_west_n_north]      += side_wind_random[wind_west_n_north]
    numValues[wind_west_n_east]       += non_dir_wind_random[wind_west_n_east]
    numValues[wind_west_n_west]       += dir_wind_random[wind_west_n_west]
    numValues[wind_west_n_south]      += side_wind_random[wind_west_n_south]
    numValues[wind_west_n_north_east] += non_dir_side_wind_random[wind_west_n_north_east]
    numValues[wind_west_n_north_west] += dir_side_wind_random[wind_west_n_north_east]
    numValues[wind_west_n_south_east] += non_dir_side_wind_random[wind_west_n_south_east]
    numValues[wind_west_n_south_west] += dir_side_wind_random[wind_west_n_south_west]

    numValues[wind_south_n_north]      += non_dir_wind_random[wind_south_n_north]
    numValues[wind_south_n_east]       += side_wind_random[wind_south_n_east]
    numValues[wind_south_n_west]       += side_wind_random[wind_south_n_west]
    numValues[wind_south_n_south]      += dir_wind_random[wind_south_n_south]
    numValues[wind_south_n_north_east] += non_dir_side_wind_random[wind_south_n_north_east]
    numValues[wind_south_n_north_west] += non_dir_side_wind_random[wind_south_n_north_west]
    numValues[wind_south_n_south_east] += dir_side_wind_random[wind_south_n_south_east]
    numValues[wind_south_n_south_west] += dir_side_wind_random[wind_south_n_south_west]
    
    return numValues

def transition_func(grid, neighbourstates, neighbourcounts, numValues, waterDrop, initNumValues):
	
    wind_direction = 'N'

    #Find cells specified for a water drop, and if correct no of iterations have occured swap them to water
	
    wetChap = (waterDrop == 0) & (grid !=6) & (grid != 3) & (initNumValues == 0.2)
    wetForest = (waterDrop == 0) & (grid !=6) & (grid != 3) & (initNumValues == 2.1)
    wetCan = (waterDrop == 0) & (grid !=6) & (grid != 3) & (initNumValues == 1.4)
	
    numValues[wetChap] -= 0.5
    numValues[wetForest] -= 0.2
    numValues[wetCan] -= 0.4

    grid[wetChap] = 7
    grid[wetForest] = 8
    grid[wetCan] = 9
	
	#on fire neighbour count
    dead_neighbours = neighbourcounts[5] + neighbourcounts[6]

	# Chaparral = state == 0, forest = state == 1, canyon = state == 2, lake = state == 3, town = state == 4
    # fire = state == 5, burnt = state == 6
    # wet chap = 7, wet forest = 8, wet canyon = 9

    # Setting thresholds up
    chapFireThreshold = 0.5
    canFireThreshold = 1.45
    forFireThreshold = 6

    # adding up depending on burning neighboars
    add_one_neighbour = (dead_neighbours == 1) & (grid !=3) & (grid != 6) & (grid != 5)
    add_two_neighbour = (dead_neighbours == 2) & (grid !=3) & (grid != 6) & (grid != 5)
    add_more_neighbour = (dead_neighbours >= 3) & (grid !=3) & (grid != 6) & (grid != 5)
	
    one_neighbour_random = np.random.uniform(0.01, 0.05, (100,100))
    two_neighbour_random = np.random.uniform(0.05, 0.07, (100,100))
    more_neighbour_random = np.random.uniform(0.08, 0.1, (100,100))
	
    numValues[add_one_neighbour] += one_neighbour_random[add_one_neighbour]
    numValues[add_two_neighbour] += two_neighbour_random[add_two_neighbour]
    numValues[add_more_neighbour] += more_neighbour_random[add_more_neighbour]

	#adding wind into the equation
    numValues = wind(wind_direction, numValues, neighbourstates, grid)
    
	# Checking values and setting states
    chap_cells = (grid == 0)
    forest_cells = (grid == 1)
    can_cells = (grid == 2)
    on_fire = (grid == 5)
	
    switch_chap_to_fire = (dead_neighbours>0) & (numValues >= chapFireThreshold) & (grid == 0)
    switch_forest_to_fire = (dead_neighbours>0) & (numValues >= forFireThreshold) & (grid == 1)
    switch_can_to_fire = (dead_neighbours>0) & (numValues >= canFireThreshold) & (grid == 2)

    switch_wet_chap_to_fire = (dead_neighbours>0) & (numValues >= forFireThreshold) & (grid == 7)
    switch_wet_forest_to_fire = (dead_neighbours>0) & (numValues >= forFireThreshold) & (grid == 8)
    switch_wet_can_to_fire = (dead_neighbours>0) & (numValues >= forFireThreshold) & (grid == 9)
	
    switch_chap_to_burnt = (dead_neighbours>0) & (numValues <= 0) & (grid==5)
    switch_forest_to_burnt = (dead_neighbours>0) & (numValues <= 0)& (grid==5)
    switch_can_to_burnt = (dead_neighbours>0) & (numValues <= 0)& (grid==5)
	
    itMult = 8
    itHours = itMult * 24
	
    chap_random = np.random.random_integers(itMult * 6, itHours * 5, (100,100))
    can_random = np.random.random_integers(itMult * 6, itMult * 18, (100,100))
    forest_random = np.random.random_integers(itHours * 15, itHours * 31, (100,100))

    numValues[switch_chap_to_fire] += chap_random[switch_chap_to_fire]
    numValues[switch_can_to_fire] += can_random[switch_can_to_fire]
    numValues[switch_forest_to_fire] += forest_random[switch_forest_to_fire]
    
    numValues[switch_wet_chap_to_fire] += chap_random[switch_wet_chap_to_fire]
    numValues[switch_wet_forest_to_fire] += forest_random[switch_wet_forest_to_fire]
    numValues[switch_wet_can_to_fire] += can_random[switch_wet_can_to_fire]
    
    numValues[on_fire] -= 1

    grid[switch_chap_to_fire] = 5
    grid[switch_forest_to_fire] = 5
    grid[switch_can_to_fire] = 5
	
    grid[switch_wet_chap_to_fire] = 5
    grid[switch_wet_forest_to_fire] = 5
    grid[switch_wet_can_to_fire] = 5
	
    grid[switch_chap_to_burnt] = 6
    grid[switch_forest_to_burnt] = 6
    grid[switch_can_to_burnt] = 6
	
    waterDrop -= 1
	
    return grid

def setup(args):
    config_path = args[0]
    config = utils.load(config_path)
    # ---THE CA MUST BE RELOADED IN THE GUI IF ANY OF THE BELOW ARE CHANGED---
    config.title = "FireStorm"
    config.dimensions = 2
    config.states = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    # ------------------------------------------------------------------------

    # ---- Override the defaults below (these may be changed at anytime) ----

    config.state_colors = [(1,1,0),(0,1,0),(0.752,0.752,0.752),(0,0,1),(0,0,0),(1,0,0), (1, 1, 1), (0.874, 0.615, 0.027), (0.137, 0.325, 0.227), (0.4, 0.4, 0.4), (135/255, 62/255, 59/255)]
    config.grid_dims = (100,100)

    # ----------------------------------------------------------------------

    if len(args) == 2:
        config.save()
        sys.exit()

    return config

first_time = True
def main():
    # Open the config object
    config = setup(sys.argv[1:])

    #create intial matrix values
    numValues = np.zeros(config.grid_dims)
    initNumValues = np.zeros(config.grid_dims)

    # setting base numbers
    forestl, forestr = 60, 30
    canl, canr = 10, 64
    townl, townr = 98, 0
	
    numValues.fill(0.2)
    numValues[forestl:forestl+20, forestr:forestr+22] = 1.9
    numValues[canl:canl+60, canr:canr+6] = 1.4
    numValues[townl:townl+2, townr:townr+5] = -2
    initNumValues = numValues
	
    #Creating the water drop matrix
    waterDrop = np.zeros(config.grid_dims)
    waterDrop.fill(-1)
	
    reactionTime = 100
    #specify the location and time of the water drop
    waterDrop[0:40, 20] = reactionTime

    grid = Grid2D(config, (transition_func, numValues, waterDrop, initNumValues))

    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()

    # save updated config to file
    config.save()
    # save timeline to file
    utils.save(timeline, config.timeline_path)


if __name__ == "__main__":
    main()
