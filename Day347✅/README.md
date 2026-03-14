# Day 347

# 1. What is Reinforcement Learning?

Reinforcement Learning is a learning paradigm where an **agent learns by interacting with an environment**.

Basic components:

| Component   | Meaning                            |
| ----------- | ---------------------------------- |
| Agent       | The learner (AI model)             |
| Environment | The world the agent interacts with |
| State (S)   | Current situation                  |
| Action (A)  | What the agent can do              |
| Reward (R)  | Feedback from environment          |
| Policy (π)  | Strategy to choose actions         |

Goal:

**Maximize total reward over time.**

Example
Robot learning to walk, game AI, recommendation systems.

---

# 2. What is Q-Learning?

Q-Learning is a **model-free reinforcement learning algorithm**.

It learns a function called **Q-function**.

This function answers:

> How good is it to take action **a** in state **s**?

---

### Q Function

Q(s,a) = \text{expected future reward when taking action } a \text{ in state } s

Meaning:

If agent is in state **s** and takes action **a**, the Q value tells the **expected reward**.

---

# 3. The Q-Learning Update Rule

This is the **heart of Q-Learning**.

Q(s,a) \leftarrow Q(s,a) + \alpha \left[r + \gamma \max_{a'} Q(s',a') - Q(s,a)\right]

Where:

| Symbol       | Meaning                                        |
| ------------ | ---------------------------------------------- |
| α            | Learning rate                                  |
| γ            | Discount factor (importance of future rewards) |
| r            | Immediate reward                               |
| s'           | Next state                                     |
| max Q(s',a') | Best possible future reward                    |

---

### Intuition

The update rule says:

> New Q = Old Q + Learning rate × (Target − Old Q)

Where

Target = reward + best future reward

So the agent slowly **improves its estimate**.

---

# 4. Q-Table

In basic Q-Learning we store values in a **table**.

Example:

| State | Left | Right |
| ----- | ---- | ----- |
| S1    | 0.1  | 0.5   |
| S2    | 0.3  | 0.2   |

Agent always picks the **highest Q value action**.

Problem:

This works only when **state space is small**.

Example:

* Grid world ✓
* Chess ✗
* Self driving ✗

---

# 5. Problem with Q-Tables

If states become huge:

Example

* Image input
* Game screen
* Robot sensors

State space becomes **millions or billions**.

Q-table becomes impossible.

So we approximate Q using **neural networks**.

---

# 6. Deep Q-Network (DQN)

A **Deep Q-Network** uses a neural network to approximate Q values.

Instead of:

```
Q-table[state][action]
```

We use:

```
Q(s,a) = NeuralNetwork(s)
```

Input:

```
State
```

Output:

```
Q value for each action
```

Example output:

```
State → [Q_left, Q_right, Q_up, Q_down]
```

---

# 7. DQN Architecture

Typical architecture:

```
State (input)
      ↓
Neural Network
      ↓
Q values for actions
```

Example:

```
State (image)

→ CNN layers
→ Dense layers

→ Output:
[Q_left, Q_right, Q_jump]
```

Agent selects:

```
argmax(Q)
```

---

# 8. Key Tricks in Deep Q-Network

To stabilize training DQN uses:

### 1️⃣ Experience Replay

Store experiences:

```
(state, action, reward, next_state)
```

Sample random batches for training.

Why?

Removes correlation between samples.

---

### 2️⃣ Target Network

Use two networks:

```
Online network
Target network
```

Target network updates slowly.

Why?

Stabilizes learning.

---

# 9. DQN Training Loop

Algorithm:

```
Initialize Q-network
Initialize replay memory

for each episode:

    observe state

    choose action (epsilon-greedy)

    execute action

    observe reward and next state

    store experience in replay memory

    sample batch

    compute target Q values

    train neural network
```

---

# 10. Exploration vs Exploitation

Agent must balance:

| Strategy     | Meaning                  |
| ------------ | ------------------------ |
| Exploration  | Try new actions          |
| Exploitation | Choose best known action |

Common method:

**ε-greedy**

```
With probability ε → random action
With probability 1−ε → best action
```

---

# 11. Real World Applications

DQN used in:

* Atari game playing
* Robotics control
* Traffic signal optimization
* Recommendation systems
* Autonomous driving

---

# 12. Simple Q-Learning Code (Python)

```python
import numpy as np

states = 5
actions = 2

Q = np.zeros((states, actions))

alpha = 0.1
gamma = 0.9

for episode in range(1000):

    state = np.random.randint(0, states)

    action = np.random.randint(0, actions)

    reward = np.random.rand()

    next_state = np.random.randint(0, states)

    Q[state, action] = Q[state, action] + alpha * (
        reward + gamma * np.max(Q[next_state]) - Q[state, action]
    )
```

This is the **core idea behind Q-learning**.

---

# 13. Big Picture

```
Reinforcement Learning
        ↓
Q Learning
        ↓
Deep Q Networks (DQN)
        ↓
Advanced RL
   • Double DQN
   • Dueling DQN
   • PPO
   • A3C
```

---