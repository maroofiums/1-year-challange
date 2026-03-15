# Day 348 - **PyGame Basics**



## **Description:**

This project demonstrates the fundamentals of **PyGame**, including creating a window, handling events, and drawing shapes. It’s designed for beginners who want to learn how to build interactive games in Python.

---

## **Features:**

* Create a game window with a custom title and size.
* Handle **user events** like closing the window.
* Draw shapes (rectangles, circles) and fill the background with colors.
* Learn the structure of a **game loop** in PyGame.

---

## **Installation**

1. Make sure you have Python installed (≥ 3.7).
2. Install PyGame using pip:

```bash
pip install pygame
```

---

## **Usage**

Run the main Python file:

```bash
python main.py
```

**Expected behavior:**

* A window opens with your chosen size and title.
* The background is colored.
* The program runs until you close the window.

---

## **Basic Example Code**

```python
import pygame

# Initialize PyGame
pygame.init()

# Create window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Basics")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with color
    screen.fill((0, 128, 255))  # Blue background
    pygame.display.flip()

# Quit
pygame.quit()
```

---

## **Learning Goals**

By running and modifying this project, you will learn:

1. PyGame initialization and quitting.
2. Window creation and updates.
3. Event handling basics.
4. Simple graphics with colors and shapes.

---
