# Thomas Schaeffer
# 10/27/23

# SOURCES
# [1] sig figs function: 
# https://gist.github.com/ttamg/3f65227fd580b3d8dc8ba91e01507280
#
# [2] GridWorld, new_state_rewards: 
# https://github.com/parasdahal/tinyrl/blob/master
#
# [3] sort dict by key:
# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/

import random as rnd
from math import floor, log10

class GridWorld:

    POSSIBLE_ACTIONS = ['up', 'down', 'left', 'right']

    def __init__(self, rewards, wall):
        """Initialize the GridWorld object

        Parameters
        ----------
        rewards: dict {state: int}
            A dictionary with reward values for each exit state in the grid

        wall_state: int
            An int representing the location of the wall in the grid
        """

        self.rewards = rewards
        self.wall = wall



    def new_state_reward(self, action, state):
        """Returns the coordinates of a resultant state and its rewards

        Parameters
        ----------
        action: str
            The string representing the action taken
        state: int
            The current state from which the action is taken

        Returns
        -------
        state: int
            The new state
        reward: int
            The reward for the new state

        """

        # new state is configured to take into account position bounds
        # also take into account if state == wall
        
        if action == 'up' and state not in [13,14,15,16]:   
            if state + 4 != self.wall:
                state = state + 4

        elif action == 'down' and state not in [1,2,3,4]:
            if state - 4 != self.wall:
                state = state -  4

        elif action == 'right' and state not in [4,8,12,16]:
            if state + 1 != self.wall:
                state = state + 1

        elif action == 'left' and state not in [1,5,9,13]:
            if state - 1 != self.wall:
                state = state - 1

        # include a -0.1 for 'living cost' every time we get a new reward
        return state, self.rewards.get(state) -0.1
    


all_actions = ['up', 'down', 'left', 'right']


def epsilon_greedy(action, epsilon):
    """Returns action according to epsilon greedy exploration scheme
    """
 
    all_actions = ['up', 'down', 'left', 'right']

    
    p = rnd.uniform(0,1)
    if p < (1 - epsilon):
        return action
    else:
        return rnd.choices(all_actions)[0]


def q_learning(env: object, num_episodes: int=10000, epsilon: int=0.5, alpha: int=0.3, gamma: int=0.1):
    """Performs q learning algorithm on given environment

    Parameters
    ----------
    env : GridWorld
        The GridWorld environment object
    num_episodes: int
        The number of episodes to run
    epsilon: float
        Epsilon value for exploration
    alpha: float
        Learning rate
    gamma : float
        Discount factor represents care for future rewards

    Returns
    -------
    sorted_policy: dict {int: str}
        The optimal policy dict with optimal action for each state
    sorted_q_vals: dict {(state, action): float}
    """

    all_actions = ['up', 'right', 'down', 'left']

    # for all our episodes, we will start in state index 2
    start_state = 2

    # initialize Q[s][a] = 0 for all state/action pairs
    Q = {}
    for state in env.rewards.keys():
        Q[state] = {}
        for action in all_actions:
            Q[state][action] = 0

    states_visited = [start_state]
    for episode in range(num_episodes):
        state = start_state
       
      
        # end state = goal1, goal2, or forbidden (only keys in rewards lib)
        while env.rewards[state]==0:

            # take best action for current state and use epsilon greedy
            action = max(Q[state], key=Q[state].get)
            action = epsilon_greedy(action, epsilon)

            # from s', find best a' and s''
            new_state, reward = env.new_state_reward(action,state)

            # calculate sample and update Q[s][a]
            best_action = max(Q[new_state], key=Q[new_state].get)
            sample = reward + gamma*Q[new_state][best_action]
            Q[state][action] = (1-alpha)*Q[state][action] + alpha*sample

            state = new_state

    # optimal policy and V
    policy, V, = {}, {}
    for state in env.rewards.keys():

        best_a = max(Q[state], key=Q[state].get)
        best_q = Q[state][best_a]

        if env.rewards[state] == 0:
            policy[state] = best_a 
            V[state] = best_q

        elif env.rewards[state] == 'wall-square':
            policy[state] = env.rewards[state]
            V[state] = env.rewards[state]
        
        elif env.rewards[state] == 100:
            policy[state] = 'goal'
            V[state] = env.rewards[state]
            
        elif env.rewards[state] == -100:
            policy[state] = 'forbid'
            V[state] = env.rewards[state]

    # [3] sort policies and q_vals for output formatting
    policy_keys = list(policy.keys())
    policy_keys.sort()
    sorted_policy = {i: policy[i] for i in policy_keys}
 
    q_val_keys = list(Q.keys())
    q_val_keys.sort()
    sorted_q_vals = {i: Q[i] for i in q_val_keys}

    return (sorted_policy, sorted_q_vals)



# -------------------------------- EVALUATE -------------------------------------

# format inputs
input = input()

if input[-1] == 'p':
    goal1, goal2, forbidden, wall, output_type = input.split(" ")
else:
    goal1, goal2, forbidden, wall, output_type, q_val_state_des  = input.split(" ")

# convert str to ints
goal1 = int(goal1)
goal2 = int(goal2)
forbidden = int(forbidden)
wall = int(wall)


#initialize environment
def grid(goal_state_1 = goal1, goal_state_2 = goal2, forbidden_state = forbidden, wall  = wall):
    """Utility function, returns 4x4 GridWorld object with rewards
    """

    wall = wall
    # dict with rewards for states of the grid

    rewards = {
        
        goal_state_1: 100,
        goal_state_2: 100,
        forbidden_state: -100,
        wall: 'wall-square'
        
    }

    for i in range(16):
        if i+1 not in rewards.keys():
            rewards[i+1] = 0     

    return GridWorld(rewards=rewards, wall=wall)



environment = grid()

# seed randomizer with value 1
rnd.seed(1)

# run q_learning to obtain optimal policy & q-vals
policy, q_vals = q_learning(grid())

# [2] round q_vals for output formatting
def sig_figs(x: float, precision: int):
    """
    Rounds a number to number of significant figures
    Parameters:
    - x - the number to be rounded
    - precision (integer) - the number of significant figures
    Returns:
    - float
    """

    
    if x == 0:
        return 0.0
    
    x = float(x)
    precision = int(precision)
    return round(x, -int(floor(log10(abs(x)))) + (precision - 1))

# check output type and print accordingly
if output_type == 'q':

    q_vals_des = q_vals[int(q_val_state_des)]

    all_actions = ['up','right','down','left']
    for action in all_actions:

        q_vals_des_rounded = sig_figs(q_vals_des[action], 2)
        
        print(action, q_vals_des_rounded)

else:
    for state in policy.keys():
        print(state, policy[state])
    
