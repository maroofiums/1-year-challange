import random

states = [(0,0),(0,1),(1,0),(1,1)]

actions = ['up','down','left','right']

Q = {}
for state in states:
    Q[state] = {}
    for action in actions:
        Q[state][action] = 0
        
alpha = 0.1
gamma = 0.9
epsilon = 0.2

def get_next_state(state, action):
    x, y = state
    if action == 'up':
        x = max(x -1, 0)
    elif action == 'down':
        x = min(x +1, 1)
    elif action == 'left':
        y = max(y -1, 0)
    elif action == 'right':
        y = min(y +1, 1)
    return (x, y)

def get_reward(state):
    if state == (1,1):
        return 10
    else:
        return -1
    
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)
    else:
        return max(Q[state], key=Q[state].get)
    
episodes = 100
for episode in range(episodes):
    state = (0,0)
    while state != (1,1):
        action = choose_action(state)
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)
        
        old_q = Q[state][action]
        next_max = max(Q[next_state].values())
        
        Q[state][action] = old_q + alpha * (reward + gamma * next_max - old_q)
        state = next_state
    
for state in Q:
    print(f"State: {state}, Q-values: {Q[state]}")
    
        