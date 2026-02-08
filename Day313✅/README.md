# Day 313

## 1️⃣ Pygame kya hota hai? (Simple words)

**Pygame = Python library for making games & simulations**

Is se hum:

* Window / screen bana sakte hain
* Shapes, images draw kar sakte hain
* Keyboard & mouse input le sakte hain
* Animations + movement bana sakte hain
* Game loop chala sakte hain

👉 **Important:**
Pygame sirf games ke liye nahi —
**Grid-world, agent movement, RL visualization** ke liye bhi use hota hai.

---

## 2️⃣ Pygame install kaise karein?

```bash
pip install pygame
```

Best practice:
Virtual environment ke andar install karo (later clean rehta hai).

---

## 3️⃣ Sab se basic pygame program (Window open)

Ye **HELLO WORLD** hai pygame ka:

```python
import pygame

# Step 1: initialize pygame
pygame.init()

# Step 2: create window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Pygame")

# Step 3: game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Step 4: update screen
    pygame.display.update()

# Step 5: quit pygame
pygame.quit()
```

### Breakdown (samajhna zaroori hai):

* `pygame.init()`
  → pygame ke saare modules start karta hai

* `set_mode((width, height))`
  → screen banata hai

* **Game loop (`while running`)**
  → ye dil hai pygame ka
  → jab tak loop chal raha, window alive hai

* `pygame.event.get()`
  → keyboard, mouse, close button sab events yahan aate hain

---

## 4️⃣ Screen fill + colors

Colors RGB mein hote hain:

```python
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
```

Use:

```python
screen.fill(WHITE)
```

⚠️ **Common mistake:**
Agar `fill()` game loop ke andar nahi likha → screen update nahi hogi properly.

---

## 5️⃣ Shapes draw karna (basic drawing)

### Rectangle:

```python
pygame.draw.rect(screen, RED, (100, 100, 50, 50))
```

Format:

```
(surface, color, (x, y, width, height))
```

👉 `(x, y)` top-left corner hota hai.

---

### Circle:

```python
pygame.draw.circle(screen, BLACK, (300, 200), 30)
```

---

## 6️⃣ Movement ka concept (VERY IMPORTANT)

Movement ka rule:

> **Position update hoti hai har frame**

Example:

```python
x = 50
y = 50
speed = 5
```

Game loop ke andar:

```python
x += speed
```

Aur draw:

```python
pygame.draw.rect(screen, RED, (x, y, 50, 50))
```

Yeh hi concept baad mein:

* player movement
* agent movement
* Q-learning actions (up/down/left/right)

---

## 7️⃣ Keyboard input (controls)

```python
keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT]:
    x -= 5
if keys[pygame.K_RIGHT]:
    x += 5
```

👉 Ye **continuous press** ke liye hota hai (smooth movement).

---

## 8️⃣ FPS control (professional cheez)

```python
clock = pygame.time.Clock()
```

Game loop ke end mein:

```python
clock.tick(60)
```

Matlab:

* 60 frames per second
* CPU zyada waste nahi hota

⚠️ FPS control **ignore mat karna**, warna system heat karega.

---

## 9️⃣ Pygame aur Q-Learning ka relation (important clarity)

Pygame:

* ❌ Q-learning ka part nahi
* ✅ Visualization tool hai

Example:

* Grid world draw karna
* Agent ko move hote dikhana
* Rewards / walls show karna

Q-learning logic:

* state
* action
* reward
* Q-table

👉 Ye **pygame ke baghair** bhi kaam karta hai.

---