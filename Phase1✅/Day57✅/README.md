# Day 57

Welcome to Day 57 of the 365 Days of Code Challenge!
Here’s a clear breakdown of **React Basics** covering **Components**, **Props**, and **State** – the building blocks of React development:

---

## 🧩 1. React Components

### What is a Component?

A **Component** is a reusable piece of UI in React. It can be a **function** or a **class**, but functional components with hooks are preferred in modern React.

### Functional Component (Preferred)

```jsx
function Welcome() {
  return <h1>Hello, World!</h1>;
}
```

### Arrow Function Version

```jsx
const Welcome = () => <h1>Hello, World!</h1>;
```

### Using Components

```jsx
function App() {
  return (
    <div>
      <Welcome />
    </div>
  );
}
```

---

## 📦 2. Props (Properties)

### What are Props?

Props are **inputs to components**. They are passed down from a parent to a child component and are **read-only**.

### Example

```jsx
function Greeting(props) {
  return <h1>Hello, {props.name}!</h1>;
}
```

### Usage

```jsx
function App() {
  return <Greeting name="Maroof" />;
}
```

### Destructuring Props

```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```

---

## 🔁 3. State

### What is State?

**State** is a built-in object used to contain data or information about the component. It can change over time and re-renders the UI when updated.

### Using `useState` Hook

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0); // [state, setState function]

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

---

## Summary Table

| Feature   | Description                           | Example                    |
| --------- | ------------------------------------- | -------------------------- |
| Component | Reusable UI block                     | `<Header />`, `<Footer />` |
| Props     | Data passed to components             | `<Greeting name="John" />` |
| State     | Component data that changes over time | `useState(0)`              |

---

