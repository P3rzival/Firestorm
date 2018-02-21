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


def transition_func(grid, neighbourstates, neighbourcounts, decaygrid):
    # dead = state == 0, live = state == 1
	# Chaparraol = state == 0, forest = state == 1, canyon = state == 2, lake = state == 3, town = state == 4
    # unpack state counts for state 0 and state 1
    cells_in_state_5 = (grid == 5)
    decaygrid[cells_in_state_5] -= 1
    decayed_to_zero = (decaygrid == 0)
    grid[decayed_to_zero] = 6

    dead_neighbours = neighbourcounts[5] #on fire neighbour count
    live_neighbours = 8 - dead_neighbours #not on fire neighbour count
    #dead_neighbours, live_neighbours = neighbourcounts
    
    # create boolean arrays for the birth & survival rules
	
    # if 3 live neighbours and is dead -> cell born
    birth = (live_neighbours == 3) & (grid == 0)
	
    #fire = (dead_neighbours >= 2) & (grid != 3)
	
    chaparralFire = (dead_neighbours >= 2) & (grid !=3) & (grid != 6)
	
    forestFire = (dead_neighbours >= 3) & (grid == 1)
	
    canyonFire = (dead_neighbours >= 1) & (grid ==2)
	
    # if 2 or 3 live neighbours and is alive -> survives
    survive = ((live_neighbours == 2) | (live_neighbours == 3)) & (grid == 1)
	
    """# Set all cells to 0 (dead)
    grid[:, :] = 5"""
	
    # Set cells to 1 where either cell is born or survives
    #grid[birth | survive] = 1
    grid[chaparralFire | forestFire | canyonFire] = 5
    return grid


def setup(args):
    config_path = args[0]
    config = utils.load(config_path)
    # ---THE CA MUST BE RELOADED IN THE GUI IF ANY OF THE BELOW ARE CHANGED---
    config.title = "Fire simulation"
    config.dimensions = 2
    config.states = (0, 1, 2, 3, 4, 5, 6)
    # ------------------------------------------------------------------------

    # ---- Override the defaults below (these may be changed at anytime) ----

    config.state_colors = [(1,1,0),(0,1,0),(0.752,0.752,0.752),(0,0,1),(0,0,0),(1,0,0), (1, 1, 1)]
    # config.num_generations = 150
    config.grid_dims = (50,50)
    config.initial_grid = np.zeros(config.grid_dims)                # zero grid
    waterl, waterr = 10, 5
    forestl, forestr = 30, 15
    canl, canr = 5, 32
    townl, townr = 49, 0
    config.initial_grid[forestl:forestl+10, forestr:forestr+11] = 1           # fill square with state 1
    config.initial_grid[waterl:waterl+4, waterr:waterr+9] = 3
    config.initial_grid[canl:canl+30, canr:canr+3] = 2
    config.initial_grid[townl:townl+1, townr:townr+3] = 4
    config.initial_grid[0,49] = 5
    config.initial_grid[1,49] = 5
	
    # ----------------------------------------------------------------------
	
    if len(args) == 2:
        config.save()
        sys.exit()

    return config


def main():
    # Open the config object
    config = setup(sys.argv[1:])

    # Create grid object
    decaygrid = np.zeros(config.grid_dims)
    decaygrid.fill(2)
    forestl, forestr = 30, 15
    canl, canr = 5, 32
    townl, townr = 49, 0
    decaygrid[forestl:forestl+10, forestr:forestr+11] = 4           # fill square with state 1 
    decaygrid[canl:canl+30, canr:canr+3] = 1
    grid = Grid2D(config, (transition_func, decaygrid))

    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()

    # save updated config to file
    config.save()
    # save timeline to file
    utils.save(timeline, config.timeline_path)


if __name__ == "__main__":
    main()
