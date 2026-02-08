# Day 312

# Q-Learning Basics (From Scratch in Python)

This project demonstrates the **basic implementation of Q-Learning** using pure Python.
No Pygame, no Gym, no ML libraries — only core Reinforcement Learning logic.

The goal is to clearly understand:
- What a Q-table is
- Why Q-values start from zero
- How an agent learns using rewards and future values

---

## Problem Setup

We use a **2x2 Grid World** environment.

### Grid
```

(0,0)  (0,1)
(1,0)  (1,1)  ← Goal

```

### Agent
- Starts at `(0,0)`
- Goal is to reach `(1,1)`

### Actions
- `up`
- `down`
- `left`
- `right`

---

## Reward System

| Situation        | Reward |
|------------------|--------|
| Reach the goal   | +10    |
| Normal move      | -1     |

This reward structure encourages the agent to reach the goal in fewer steps.

---

## Q-Learning Concept

Q-Learning learns a function:

```

Q(state, action)

```

Meaning:
> How good is it to take a specific action in a given state?

All Q-values start with **0** because the agent initially has **no knowledge** of the environment.

---

## Q-Learning Formula

```

Q(s, a) = Q(s, a) + α [ r + γ max(Q(s', a')) − Q(s, a) ]

```

### Parameters
- `α (alpha)` → Learning rate (how fast the agent learns)
- `γ (gamma)` → Discount factor (importance of future reward)
- `ε (epsilon)` → Exploration rate (random vs best action)

---

## Training Process

1. Start from `(0,0)`
2. Choose an action using ε-greedy strategy
3. Move to the next state
4. Receive a reward
5. Update the Q-table
6. Repeat for multiple episodes

Over time, the agent learns the **optimal path** to the goal.

---

## Files

```

q_learning_basic.py
README.md

````

---

## How to Run

```bash
python q_learning_basic.py
````

After training, the final Q-table will be printed in the terminal.

---

## Key Observations

* Actions leading to the goal get higher Q-values
* Wrong or inefficient actions get lower or negative values
* Learning happens **without labeled data**

---

## Why No Pygame or Gym?

This project focuses on **concept clarity**.
Visualization is optional and can be added later once the logic is clear.

---

## Who Is This For?

* Beginners in Reinforcement Learning
* Students learning RL theory
* Anyone confused about Q-tables and updates

---
