# Q-Learning in GridWorld

This project implements tabular **Q-Learning** to derive an optimal policy in a custom 4x4 GridWorld environment with goals, walls, and penalties. The agent learns to navigate the grid by maximizing cumulative reward under an epsilon-greedy exploration policy.

> Developed by Thomas Schaeffer  
> Date: 10/27/2023  
> Project: AI Homework 3

---

## Goal

Learn an optimal action policy in a discrete 4x4 grid by applying the Q-learning algorithm. The environment includes two goal states (+100), one forbidden state (–100), and a wall (impassable).

---

## Methods

- **Environment**: Custom GridWorld class with adjustable reward states and wall locations  
- **Q-Learning**:  
  - Epsilon-greedy exploration  
  - Learning rate α = 0.3  
  - Discount factor γ = 0.1  
  - 10,000 episodes from fixed start state  
- **Reward structure**:  
  - +100 for goal states  
  - –100 for forbidden state  
  - –0.1 living cost for each step  
- Outputs:
  - Optimal policy per state  
  - Q-values for selected state/action pairs  

---

## Results

- Agent learns to avoid forbidden and wall states while navigating efficiently toward goals  
- Final policy reflects shortest valid paths under stochastic action selection  
- Q-values converge after repeated exploration (10k episodes, seeded randomness)

Example output:

```bash
# Optimal Policy
1 right  
2 right  
3 right  
4 goal  
...

# Q-values for State 5
up 0.56  
right 1.2  
down -2.3  
left 0.15
