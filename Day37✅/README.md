# Day 37

Here’s a beginner-friendly overview of **React Basics** using **Vite**, covering **Components**, **Props**, and **State**:

---

### ✅ 1. Setting Up React with Vite

**Step 1: Create Project**

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

---

### ✅ 2. React Components

**What are Components?**
Components are reusable pieces of UI in React. There are two types:

* **Functional Components** (most common now)
* Class Components (used in older React)

#### Example:

```jsx
// src/components/Greeting.jsx
function Greeting() {
  return <h1>Hello, Maroof!</h1>;
}

export default Greeting;
```

```jsx
// src/App.jsx
import Greeting from './components/Greeting';

function App() {
  return (
    <div>
      <Greeting />
    </div>
  );
}

export default App;
```

---

### ✅ 3. Props (Properties)

**What are Props?**
Props are used to pass data **from parent to child** components.

#### Example:

```jsx
// src/components/User.jsx
function User(props) {
  return <h2>Welcome, {props.name}!</h2>;
}

export default User;
```

```jsx
// src/App.jsx
import User from './components/User';

function App() {
  return (
    <div>
      <User name="Maroof" />
      <User name="Tanvir" />
    </div>
  );
}
```

---

### ✅ 4. State

**What is State?**
State is used to store dynamic data and re-render the UI when it changes.

#### Example:

```jsx
// src/components/Counter.jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increase</button>
    </div>
  );
}

export default Counter;
```

```jsx
// src/App.jsx
import Counter from './components/Counter';

function App() {
  return (
    <div>
      <Counter />
    </div>
  );
}
```

---

### 🧠 Summary

| Concept   | Purpose                      | Syntax                       |
| --------- | ---------------------------- | ---------------------------- |
| Component | Build UI blocks              | `function MyComponent() {}`  |
| Props     | Pass data to components      | `<Component name="value" />` |
| State     | Handle dynamic/changing data | `useState(initialValue)`     |

---

Would you like a small practice project using these basics (like a ToDo app or Product card)?
