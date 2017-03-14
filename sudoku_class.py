import sys
sys.path.append('./aima/')
import search
from search import *
import utils
import sudoku_script as ss

class Sudoku(search.Problem):

    """The abstract class for a formal problem.  You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = ss.str_to_grid(initial)
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        result = []
        for x in range(0, 8):
            for y in range(0, 8):
                pos = ss.eval_possibility(x, y, state)
                if len(pos) > 1:
                    for z in pos:
                        action = str(z) + str(x) + str(y)
                        result.append(action)
        return result
        #Si l'action est 301 alors on place 3 a la deuxieme colonne de la premiere rangee

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        next_state = ss.add_to_grid(int(action[0]), int(action[1]), int(action[2]), state)
        return next_state

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        #if isinstance(self.goal, list):
           # return utils.is_in(state, self.goal)
        #else:
         #   return state == self.goal
        goal = True
        for x in range (0,8):
            for y in range (0,8):
                if state[x][y] == 0:
                    goal = False
                    break
                if ((not ss.check_line(state[x][y],x,y,state)) or (not ss.check_square(state[x][y],x,y,state))):
                    goal = False
                    break
        return goal
    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError