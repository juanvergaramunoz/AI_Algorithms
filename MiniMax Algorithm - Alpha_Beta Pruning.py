
class CustomPlayer:
    """ MiniMax Agent. Could be used to play Isolation, Chess, Go,...
        
    There are several assumptions (in terms of classes and procesures) made.
    This was required to show only the MiniMax part of the whole algorithm:

    **********************************************************************
    NOTE:
    - A function is called to select the action - f.i: "put_action(ACTION)"
    - It can be called several times
    - The last one put before the timer goes off (f.i: 2 secs) is the one selected
    - We assume the function calling is the one that takes care of the timer from
        the moment it calls this function (to keep things simple).
    
    ALSO NOTE:
    - The valid actions per player are given by "state.actions()"
        * It returns an array of actions
    - We assume the result of applying an action is given by "state.result(action)"
        * When applied, it automatically changes the player's turn
    - Lastly, the EVALUATION of a terminal state is given by "state.utility(PLAYER)"
        * 'PLAYER' is a binary element and it is retrieve calling "state.player()"
    **********************************************************************
    """
    
    def get_action(self, state, put_action):
        """ Calls put_action(ACTION) at least once, before the algorithm
        runs out of time (f.i: 2 secs). We assume the caller will be responsible
        for cutting off the function after the search time limit has expired.
        """
        
        import random
        
        #WE PUT A RANDOM ACTION FIRST (to assure at least one action is placed in time)
        actions = state.actions()
        put_action(random.choice(actions))
            
        for depth in range(10):
            alpha = float("-inf")
            beta = float("inf")

            actions = state.actions()
            main_action = None
            maximum = float("-inf")
            for i in range(len(actions)):
                new_state = state.result(actions[i])
                value = self.min_val(new_state, alpha, beta, depth-1)

                if value > maximum:
                    main_action = actions[i]

                #NEVER ENTERS HERE AS BETA IS GOING TO BE ALWAYS "INF" FOR THE ROOT NODE
                #if maximum > beta:
                #    main_action = actions[i]
                alpha = max(maximum,alpha)
            
            if main_action != None:
                put_action(main_action)
        
        return
        
        
    def min_val(self, state, alpha, beta, depth):
        """ MIN FUNCTION
        
        Minimizes the value of the Main player (as it is the other player's
        turn). It is called on the turn of the 2nd player (the one not located
        on the root of the tree)

        **********************************************************************
        NOTE: 
        - NON-TERMINAL STATE: The EVALUATION FUNCTION for a state is the number
        of actions it has available for that player.
        
        - TERMINAL STATE: We assume that it returns "inf" for winning cases and
        "-inf" for losing ones.
            
            * The player whose turn we are analizing is received through:
                "state.player()"
                
            * The function to get the value for a terminal state is:
                "state.utility(player_num)"
                
            * For non-terminal states, remember that the amount of possible
                actions is given by: "state.actions()"
        **********************************************************************
        """
        if state.utility(state.player()):
            return state.utility(not state.player())
            
        if depth < 1:
            return -len(state.actions())
        
        actions = state.actions()
        minimum = float("inf")
        for i in range(len(actions)):
            new_state = state.result(actions[i])
            value = self.max_val(new_state, alpha, beta, depth-1)
            
            minimum = min(value, minimum)
            
            if minimum < alpha:
                return minimum
            beta = min(minimum,beta)
        
        return minimum
        pass    
    
    def max_val(self, state, alpha, beta, depth):
        """ MAX FUNCTION
        
        Maximizes the value of the main player. It is called on the turn of
        the player located on the root of the tree

        **********************************************************************
        NOTE: 
        - NON-TERMINAL STATE: The EVALUATION FUNCTION for a state is the number
        of actions it has available for that player.
        
        - TERMINAL STATE: We assume that it returns "inf" for winning cases and
        "-inf" for losing ones.
            
            * The player whose turn we are analizing is received through:
                "state.player()"
                
            * The function to get the value for a terminal state is:
                "state.utility(player_num)"
                
            * For non-terminal states, remember that the amount of possible
                actions is given by: "state.actions()"
        **********************************************************************
        """
        if state.utility(state.player()):
            return state.utility(state.player())
            
        if depth < 1:
            return len(state.actions())
        
        actions = state.actions()
        maximum = float("-inf")
        for i in range(len(actions)):
            new_state = state.result(actions[i])
            value = self.min_val(new_state, alpha, beta, depth-1)
            
            maximum = max(value, maximum)
            
            if maximum > beta:
                return maximum
            alpha = max(maximum,alpha)
        
        return maximum
        pass  
