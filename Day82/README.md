# 🧠 Day 82 — **Python Basics for Full-Stack Devs**

### 🎯 Goal:

Sharpen your Python fundamentals needed for Django backend.

---

## ✅ 1. Loops & Conditionals

```python
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

---

## ✅ 2. Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Maroof"))
```

---

## ✅ 3. Lists & Dictionaries

```python
products = [
    {"name": "Phone", "price": 30000},
    {"name": "Laptop", "price": 80000},
]

for product in products:
    print(product["name"], "-", product["price"])
```

---

## ✅ 4. OOP (Object-Oriented Programming)

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        return f"{self.name} - PKR {self.price}"

p1 = Product("Camera", 50000)
print(p1.show())
```

---

## 🧪 Practice Exercises for You:

1. Write a function to calculate the factorial of a number.
2. Create a list of numbers and print only the even ones.
3. Make a class `User` with name, email and a method `display()`.

