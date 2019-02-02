import random
import math

class Tree_Node_Class:
    """ Auxiliary Class for the MONTE CARLO TREE SEARCH ALGORITHM. 
    """
    def __init__(self, state, actions, action = None):
        
        self.state = state
        self.player = state.player()
        
        self.parent = None
        self.children = []
        
        self.action = action
        self.all_actions = actions
        
        self.n_visited = 0
        self.q_value = 0
        #STATE.UTILITY returns 0 for non-terminal states, "-inf"/"inf" for terminal
        self.score = state.utility(self.player)
    
    
    def get_state(self):
        return self.state
    
    
    def get_n_visited(self):
        return self.n_visited
    
    
    def get_q_value(self):
        return self.q_value
    
    
    def backup_n_and_q(self, delta_q):
        self.n_visited += 1
        self.q_value += delta_q
        return
    
    
    def is_terminal(self):
        if self.score != 0:
            return True
        return False
    
    
    def is_fully_expanded(self):
        if len(self.all_actions):
            return False
        return True
    
    
    def add_child(self):
        
        n = len(self.all_actions)
        
        ##IF THERE ARE NO MORE ACTIONS LEFT, WE END
        if not n:
            return None
        
        ##IF THERE ARE MORE ACTIONS LEFT, WE PICK A RANDOM ONE
        index = random.choice(range(n))
        new_action = self.all_actions.pop(index)
        new_state = self.state.result(new_action)
        all_actions = new_state.actions()
        
        new_node = Tree_Node_Class(new_state, all_actions, new_action)
        new_node.parent = self
        
        self.children.append(new_node)
        
        return new_node
    
    
    
    
class MCTSCustomPlayer:
    """ MONTE CARLO TREE SEARCH Agent. Could be used to play Isolation,
    Chess, Go,...
        
    There are several assumptions (in terms of classes and procesures) made.
    This was required to show only the MCTS part of the whole algorithm:

    **********************************************************************
    NOTE:
    - A function is called to select the action - f.i: "queue.put(ACTION)"
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
    
    def get_action(self, state, put_function = queue.put):
        """ Calls put_action(ACTION) at least once, before the algorithm
        runs out of time (f.i: 2 secs). We assume the caller will be responsible
        for cutting off the function after the search time limit has expired.
        """
        
        import random
        
        ## WE PUT A RANDOM ACTION FIRST
        ### To assure at least one action is placed in time
        actions = state.actions()
        if len(actions) > 0:
            r_action = random.choice(actions)
            put_function(r_action)
        else:
            r_action = 0
            put_function(r_action)
            return
        
        MC_Tree_Node = Tree_Node_Class(state, actions)
        
        prev_node = None
        new_node = MC_Tree_Node
        while prev_node != new_node:
            
            prev_node = new_node
            
            new_node = self.TreePolicy(MC_Tree_Node)
            delta = self.DefaultPolicy(new_node.state)
            self.Backup(new_node,delta)
            
            r_node = self.BestChild(MC_Tree_Node, 0)
            if r_node != None:
                r_action = r_node.action
                put_function(r_action)
        
        r_node = self.BestChild(MC_Tree_Node, 0)
        if r_node != None:
            r_action = r_node.action
            put_function(r_action)
        
        return
    
    
    
    def TreePolicy(self, node):
        """ This function is the main part of the Monte Carlo Tree Search (MCTS)
        It starts with the root node, and expands until all actions have been
        explored. From there, it starts selecting the following action with a better
        performance (more winnings encountered). The process is repeated, and
        the tree is always expanded towards the most promising node.
        """
        
        current_node = node
        while not current_node.is_terminal():
            
            if not current_node.is_fully_expanded():
                return self.Expand(current_node)
            
            else:
                current_node = self.BestChild(current_node, math.sqrt(2))
            
        return current_node
    
    
    
    def Expand(self, node):
        """ This node is the one in charge of the expansion. The main idea is to
        take one non-explored action for the Node passed as a parameter, and
        expand the Tree accordingly. To keep things simple, we have opted to
        maintain the core operations inside the TREE_NODE_CLASS. In the end, all
        the information required is already stored inside the object anyway:
        The object is the one that has the list of non-used actions, and selects
        one of them randomly.
        """
        
        current_node = node
        
        new_node = current_node.add_child()
        
        return new_node
    
    
    
    def BestChild(self, parent, cost):
        """ This function is the one in charge of picking up the most valuable
        children for the node passed. It is used to pick the best action from
        the root node, but also to pick the best node to expand for a given node.
        """
        
        max_val = float("-inf")
        best_node = None
        for child in parent.children:
            child_val = child.get_q_value()/child.get_n_visited()
            aux_val = 2*math.log(parent.get_n_visited())/child.get_n_visited()
            child_val += cost*math.sqrt(aux_val)
            
            if child_val > max_val:
                max_val = child_val
                best_node = child
            
        return best_node
    
    
    
    def DefaultPolicy(self, state):
        """ Default Policy is the function in charge of simulating the data.
        It takes random actions from the state given until it reaches a final
        state. Then, the result for the PARENT of the state is returned.
        In this implementation, winnings and losses from one state are referred
        to its parent, that is why the logic is inverse (winning has a lower
        score than losing).
        
        **********************************************************************
        NOTE:
        - STATE.utility(player): Function that returns "+inf" for a winning
        scenario for 'PLAYER' [A BOOLEAN], "-inf" for a losing scenario for
        'PLAYER'.
        **********************************************************************
        """
        new_state = state
        #
        ini_state_player = new_state.player()
        #
        while new_state.utility(new_state.player()) == 0:
            new_action = random.choice(new_state.actions())
            new_state = new_state.result(new_action)
        
        utility = new_state.utility(ini_state_player)
        if utility < 0:
            return 1
        elif utility > 0:
            return -1
        else:
            None
    
    
    
    def Backup(self, node, delta):
        """ This function is the one that stores the information collected for
        each new node expanded and its subsequent parents. It receives the node
        and the winning or loss value (+1 or -1), updates the Q and N values for
        that node, and moves into its parent.
        
        The main updating is carried out by the TREE_NODE_CLASS. This is the
        one that performs the inner update with the previous information that
        it already has stored internally (as elements inside the object node).
        """
        
        current_node = node
        while current_node != None:
            current_node.backup_n_and_q(delta)
            delta = -delta
            current_node = current_node.parent
        
        return
        

    
    
