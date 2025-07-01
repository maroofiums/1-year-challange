# Day 83

### 🔧 Project: Simple Counter App (DOM Manipulation)

---

### 📄 `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Counter App</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div class="container">
    <h1>Counter App</h1>
    <h2 id="count">0</h2>
    <div class="buttons">
      <button id="decrease">Decrease</button>
      <button id="reset">Reset</button>
      <button id="increase">Increase</button>
    </div>
  </div>
  <script src="script.js"></script>
</body>
</html>
```

---

### 🎨 `style.css`

```css
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

.container {
  background: white;
  padding: 30px;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  margin-bottom: 10px;
}

h2 {
  font-size: 48px;
  margin: 20px 0;
}

button {
  padding: 10px 20px;
  margin: 5px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #ddd;
}
```

---

### 📜 `script.js`

```javascript
let count = 0;

const countDisplay = document.getElementById("count");
const increaseBtn = document.getElementById("increase");
const decreaseBtn = document.getElementById("decrease");
const resetBtn = document.getElementById("reset");

increaseBtn.addEventListener("click", () => {
  count++;
  updateDisplay();
});

decreaseBtn.addEventListener("click", () => {
  count--;
  updateDisplay();
});

resetBtn.addEventListener("click", () => {
  count = 0;
  updateDisplay();
});

function updateDisplay() {
  countDisplay.textContent = count;
}
```

---

### ✅ What You Learn:

* Selecting elements with `getElementById`
* Adding event listeners
* Manipulating DOM content with `textContent`
* Basic styling with CSS
