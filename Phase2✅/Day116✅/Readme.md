# **Day 116**

## 🔁 **React Hooks Overview**

Hooks let you use **state** and other **React features** without writing a class.

### ✅ Commonly Used Hooks

| Hook                    | Purpose                                                         |
| ----------------------- | --------------------------------------------------------------- |
| `useState()`            | Add state to functional components                              |
| `useEffect()`           | Side effects (API calls, DOM updates, subscriptions)            |
| `useContext()`          | Access context values (global state)                            |
| `useRef()`              | Reference DOM elements or persist values across renders         |
| `useReducer()`          | Complex state logic (alternative to useState)                   |
| `useMemo()`             | Memoize expensive calculations                                  |
| `useCallback()`         | Memoize functions (to prevent re-creation)                      |
| `useLayoutEffect()`     | Like `useEffect`, but fires synchronously after DOM mutations   |
| `useImperativeHandle()` | Customizing the instance value that is exposed when using `ref` |

---

## 🎯 **Practical Examples**

### 1. `useState` Example

```jsx
const [count, setCount] = useState(0);
```

### 2. `useEffect` Example

```jsx
useEffect(() => {
  fetchData();
}, []); // Runs once on mount
```

### 3. `useContext` Example

```jsx
const theme = useContext(ThemeContext);
```

---

## 🔥 Advanced State Management

### ✅ When to use more advanced state management?

* State shared across multiple components
* Complex state logic
* Deeply nested state objects
* Async state updates (e.g., API responses)

---

## ⚙️ Tools for Advanced State Management

### 1. **useReducer**

* Good for complex local component logic

```jsx
const reducer = (state, action) => {
  switch (action.type) {
    case 'INCREMENT': return { count: state.count + 1 };
    default: return state;
  }
};
const [state, dispatch] = useReducer(reducer, { count: 0 });
```

---

### 2. **Context API (Global State for Small/Medium apps)**

* Combine with `useReducer` or `useState`

```jsx
export const AppContext = createContext();

const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};
```

---

### 3. **Third-Party State Management Libraries**

#### 🔷 Redux (Most Popular)

* Global store, middleware, dev tools
* Pair with `@reduxjs/toolkit` (RTK) for simplified setup

#### 🔶 Zustand (Minimal, simple)

```js
import create from 'zustand'

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}));
```

#### ⚛️ Recoil (Facebook's experimental state)

* Works well with React’s concurrent mode

#### ⚡ Jotai, XState, MobX, Valtio (for more niche or reactive use-cases)

---


## 🚀 Bonus: Custom Hooks

```js
function useFetch(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url).then(res => res.json()).then(setData);
  }, [url]);

  return data;
}
```

