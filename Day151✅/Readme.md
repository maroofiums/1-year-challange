# Day151
---

# ✅ **React Hooks & Advanced State Management**

---

## 🔹 1. **React Hooks – Core Hooks**

| Hook          | Purpose                                            |
| ------------- | -------------------------------------------------- |
| `useState`    | Add state to functional components                 |
| `useEffect`   | Side effects (API calls, subscriptions, etc.)      |
| `useContext`  | Access global data without prop drilling           |
| `useRef`      | Mutable references (DOM refs, persistent values)   |
| `useMemo`     | Memoize expensive computations                     |
| `useCallback` | Memoize callback functions                         |
| `useReducer`  | Like `useState` but better for complex state logic |

---

## 🔸 2. **Common Examples**

### 📌 `useState` – Basic State

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

---

### 📌 `useEffect` – API Call

```jsx
import { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []); // Runs once after mount

  return (
    <ul>
      {users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
}
```

---

### 📌 `useContext` – Global State

```jsx
// Context.js
import { createContext } from 'react';
export const ThemeContext = createContext();

// App.js
<ThemeContext.Provider value={"dark"}>
  <Header />
</ThemeContext.Provider>

// Header.js
import { useContext } from 'react';
import { ThemeContext } from './Context';

function Header() {
  const theme = useContext(ThemeContext);
  return <h1>Theme: {theme}</h1>;
}
```

---

### 📌 `useReducer` – Complex State

```jsx
import { useReducer } from 'react';

const reducer = (state, action) => {
  switch(action.type) {
    case 'increment': return { count: state.count + 1 };
    case 'decrement': return { count: state.count - 1 };
    default: return state;
  }
};

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return (
    <>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({type: 'increment'})}>+</button>
      <button onClick={() => dispatch({type: 'decrement'})}>-</button>
    </>
  );
}
```

---

### 📌 `useRef` – Access DOM

```jsx
import { useRef } from 'react';

function FocusInput() {
  const inputRef = useRef();

  const focus = () => inputRef.current.focus();

  return (
    <>
      <input ref={inputRef} />
      <button onClick={focus}>Focus</button>
    </>
  );
}
```

---

## 🔥 3. **Advanced State Management Techniques**

### ✅ Global State Options:

| Tool            | Description                                       |
| --------------- | ------------------------------------------------- |
| **Context API** | Built-in, for small global state                  |
| **Redux**       | Predictable state container for large apps        |
| **Zustand**     | Lightweight state management (modern alternative) |
| **Recoil**      | Facebook's global state with atom-based logic     |
| **Jotai**       | Minimal, atomic state management                  |

---

## 📦 Redux (Simplified Example)

```jsx
// store.js
import { createStore } from 'redux';

const reducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case "INC": return { count: state.count + 1 };
    default: return state;
  }
};

export const store = createStore(reducer);
```

```jsx
// App.js
import { Provider, useDispatch, useSelector } from 'react-redux';
import { store } from './store';

function Counter() {
  const count = useSelector(state => state.count);
  const dispatch = useDispatch();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch({ type: "INC" })}>+</button>
    </div>
  );
}

export default function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
}
```

---

## 📚 Learning Resources

| Resource           | Link                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------- |
| React Docs (Hooks) | [https://reactjs.org/docs/hooks-intro.html](https://reactjs.org/docs/hooks-intro.html) |
| Redux Toolkit      | [https://redux-toolkit.js.org/](https://redux-toolkit.js.org/)                         |
| Zustand            | [https://zustand-demo.pmnd.rs/](https://zustand-demo.pmnd.rs/)                         |
| Recoil             | [https://recoiljs.org/](https://recoiljs.org/)                                         |

