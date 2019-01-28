# Software Engineering - Artificial Intelligence -> juanvergaramunoz, 01/23/2019


** Project: Artificial Intelligence Examples
** Creator: juanvergaramunoz
** Year: 2019


## Description

This Software Engineering repository includes general examples of Artificial Intelligence algorithms

The target of this project is to provide a set of Artificial Intelligence tools (still in development)


**This project has the following CLASSES:**

1) "MiniMax Algorithm - Alpha_Beta Pruning.py" has the "CustomPlayer" Class -- FUNCTIONS:
    
       - get_action(self, state, put_action)  [USER FUNCTION]
            It provides the MiniMax Functionality with ALPHA-BETA PRUNING. Some assumptions are made:
            Read document for more detail
            
            STATE: Refers to an object that contains all information about the current board (state)
            PUT_ACTION: A function that is called with the chosen action as a parameter
       
       - min_val(self, state, alpha, beta, depth)  [INTERNAL FUNCTION]
       
       - max_val(self, state, alpha, beta, depth)  [INTERNAL FUNCTION]


2) "Genetic Algorithm.ipynb" has the "n_queen_solver" Class -- FUNCTIONS:
    
       - __init__(self, board_size, n_pair_of_parents, n_children, mutation_factor = 100) [USER FUNCTION]
            It provides the Genetic Algorithm as a CLASS for the N_QUEENS Problem
            
            BOARD_SIZE: INTEGER - Refers to the size of the N_QUEENS board [f.i: 4]
            N_PAIR_OF_PARENTS: INTEGER - Amount of pair of parents to be kept from one iteration to another [f.i: 2]
            N_CHILDREN: INTEGER - Amount of children to be created from one generation to the next [f.i: 4]
            MUTATION_FATOR: INTERGER - Amount of children per one mutation in average [f.i.: 1 mutation per 6 children == 6]
       
       - _initiate_parents(self)  [INTERNAL FUNCTION]
       
       - _get_score(self, board)  [INTERNAL FUNCTION]
       
       - _get_attacks(self, board)  [INTERNAL FUNCTION]
       
       - select_parents(self)  [PSEUDO-INTERNAL FUNCTION]
       
       - create_children(self, parent_list)  [PSEUDO-INTERNAL FUNCTION]
       
       - mutation_step(self, board)  [PSEUDO-INTERNAL FUNCTION]
       
       - execute_one_generation(self)  [PSEUDO-INTERNAL FUNCTION]
       
       - find_best(self)  [PSEUDO-INTERNAL FUNCTION]
       
       - execute_algorithm(self, n_generations = 100)
            It executes the algorithm for the consecutive generations desired
            
            N_GENERATIONS: INTEGER - Amount of times to execute the algorithm [f.i: 100]
 
 


    
