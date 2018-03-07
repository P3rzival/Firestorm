# Name: Conway's game of life
# Dimensions: 2

# --- Set up executable path, do not edit ---
import sys
import inspect
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


def transition_func(grid, neighbourstates, neighbourcounts, numValues):
    #SET TO BURNT OUT
    #cells_in_state_5 = (grid == 5)
    #decaygrid[cells_in_state_5] += 2

    #decayed_to_zero = (decaygrid >= 6)
    #grid[decayed_to_zero] = 6

    dead_neighbours = neighbourcounts[5] #on fire neighbour count
    wind_direction = 'N'

    #chaparralFire = (dead_neighbours >= 2) & (grid !=3) & (grid != 6)

    # dead = state == 0, live = state == 1
	# Chaparral = state == 0, forest = state == 1, canyon = state == 2, lake = state == 3, town = state == 4
    # unpack state counts for state 0 and state 1

    # Setting threslhods up
    chapFireThreshold = 0.4
    canFireThreshold = 0.4
    forFireThreshold = 0.6

    chapBurntThreshold = 0.4
    canBurntThreshold = 0.4
    forBurntThreshold = 0.6

    # adding up depending on burning neighboars
    add_one_neighbour = (dead_neighbours == 1) & (grid !=3) & (grid != 6)
    add_two_neighbour = (dead_neighbours == 2) & (grid !=3) & (grid != 6)
    add_more_neighbour = (dead_neighbours >= 3) & (grid !=3) & (grid != 6)

    numValues[add_one_neighbour] += 0.1
    numValues[add_two_neighbour] += 0.3
    numValues[add_more_neighbour] += 0.5

    # adding up depending on wind and neighboar
    wind_north_n_north = (wind_direction == 'N') & (neighbourstates[0] == 5)
    wind_north_n_east = (wind_direction == 'N') & (neighbourstates[4] == 5)
    wind_north_n_west = (wind_direction == 'N') & (neighbourstates[3] == 5)
    wind_north_n_south = (wind_direction == 'N') & (neighbourstates[6] == 5)
    
    wind_east_n_north = (wind_direction == 'E') & (neighbourstates[0] == 5)
    wind_east_n_east = (wind_direction == 'E') & (neighbourstates[4] == 5)
    wind_east_n_west = (wind_direction == 'E') & (neighbourstates[3] == 5)
    wind_east_n_south = (wind_direction == 'E') & (neighbourstates[6] == 5)

    wind_west_n_north = (wind_direction == 'W') & (neighbourstates[0] == 5)
    wind_west_n_east = (wind_direction == 'W') & (neighbourstates[4] == 5)
    wind_west_n_west = (wind_direction == 'W') & (neighbourstates[3] == 5)
    wind_west_n_south = (wind_direction == 'W') & (neighbourstates[6] == 5)

    wind_south_n_north = (wind_direction == 'S') & (neighbourstates[0] == 5)
    wind_south_n_east = (wind_direction == 'S') & (neighbourstates[4] == 5)
    wind_south_n_west = (wind_direction == 'S') & (neighbourstates[3] == 5)
    wind_south_n_south = (wind_direction == 'S') & (neighbourstates[6] == 5)

    numValues[wind_north_n_north] += 0.1
    numValues[wind_north_n_east] += 0.1
    numValues[wind_north_n_west] += 0.1
    numValues[wind_north_n_south] += 0.1
    numValues[wind_east_n_north] += 0.1
    numValues[wind_east_n_east] += 0.1
    numValues[wind_east_n_west] += 0.1
    numValues[wind_east_n_south] += 0.1
    numValues[wind_west_n_north] += 0.1
    numValues[wind_west_n_east] += 0.1
    numValues[wind_west_n_west] += 0.1
    numValues[wind_west_n_south] += 0.1
    numValues[wind_south_n_north] += 0.1
    numValues[wind_south_n_east] += 0.1
    numValues[wind_south_n_west] += 0.1
    numValues[wind_south_n_south] += 0.1

    # Checking values and setting states
    chap_cells = (grid == 0)
    forest_cells = (grid == 1)
    can_cells = (grid == 2)

    switch_chap_to_fire = (numValues[chap_cells] > chapFireThreshold)
    switch_forest_to_fire = (numValues[forest_cells] > forFireThreshold)
    switch_can_to_fire = (numValues[can_cells] > canFireThreshold)

    switch_chap_to_burnt = (numValues[chap_cells] > chapBurntThreshold)
    switch_forest_to_burnt = (numValues[forest_cells] > forBurntThreshold)
    switch_can_to_burnt = (numValues[can_cells] > canBurntThreshold)

    grid[switch_chap_to_fire] = 5
    grid[switch_forest_to_fire] = 5
    grid[switch_can_to_fire] = 5

    grid[switch_chap_to_burnt] = 6
    grid[switch_forest_to_burnt] = 6
    grid[switch_can_to_burnt] = 6

    #SET TO BURNING
    #decaygrid[chaparralFire] -= 1

    #decayed_to_zero2 = (decaygrid == 0)
    #grid[decayed_to_zero2] = 5

    return grid


def setup(args):
    config_path = args[0]
    config = utils.load(config_path)
    # ---THE CA MUST BE RELOADED IN THE GUI IF ANY OF THE BELOW ARE CHANGED---
    config.title = "FireStorm"
    config.dimensions = 2
    config.states = (0, 1, 2, 3, 4, 5, 6)
    # ------------------------------------------------------------------------

    # ---- Override the defaults below (these may be changed at anytime) ----

    config.state_colors = [(1,1,0),(0,1,0),(0.752,0.752,0.752),(0,0,1),(0,0,0),(1,0,0), (1, 1, 1)]
    # config.num_generations = 150
    config.grid_dims = (100,100)
    config.initial_grid = np.zeros(config.grid_dims)                # zero grid
    waterl, waterr = 20, 10
    forestl, forestr = 60, 30
    canl, canr = 10, 64
    townl, townr = 98, 0
    config.initial_grid[forestl:forestl+20, forestr:forestr+22] = 1           # fill square with state 1
    config.initial_grid[waterl:waterl+8, waterr:waterr+18] = 3
    config.initial_grid[canl:canl+60, canr:canr+6] = 2
    config.initial_grid[townl:townl+2, townr:townr+6] = 4

	#incinerator
    config.initial_grid[0,99] = 5
    config.initial_grid[1,99] = 5

	#powerplant
    #config.initial_grid[0,0] = 5
    #config.initial_grid[1,0] = 5


    # ----------------------------------------------------------------------

    if len(args) == 2:
        config.save()
        sys.exit()

    return config


def main():
    # Open the config object
    config = setup(sys.argv[1:])

    # Create grid object
    #decaygrid = np.zeros(config.grid_dims)
    #decaygrid.fill(2)

    #create intial matrix values
    numValues = np.zeros(config.grid_dims)

    # setting base numbers
    forestl, forestr = 60, 30
    canl, canr = 10, 64
    numValues.fill(0.3)
    numValues[forestl:forestl+20, forestr:forestr+22] = 0.1
    numValues[canl:canl+60, canr:canr+6] = 0.5

    #decaygrid[forestl:forestl+20, forestr:forestr+22] = 4           # fill square with state 1
    #decaygrid[canl:canl+60, canr:canr+6] = 1

    grid = Grid2D(config, (transition_func, numValues))

    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()

    # save updated config to file
    config.save()
    # save timeline to file
    utils.save(timeline, config.timeline_path)


if __name__ == "__main__":
    main()
