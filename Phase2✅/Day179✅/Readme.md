## Day179

### ⚡ React Hooks 101

Hooks are basically functions that let you use React features without writing a class.
The ones you’ll use the most:

* **`useState`** → for local component state (like toggles, inputs, counters)
* **`useEffect`** → run side effects (API calls, subscriptions, timers)
* **`useContext`** → share state across components without prop-drilling
* **`useReducer`** → a more structured way to manage complex state (like Redux-lite)
* **`useMemo`** & **`useCallback`** → performance optimization (avoid re-renders)

---

### ⚡ State Management Levels

Think of it like layers of responsibility:

1. **Local State (small stuff)**

   * `useState` is enough.
   * Example: handling form inputs or toggling a modal.

2. **Shared State (passing between siblings)**

   * `useContext` + `useReducer` combo works fine.
   * Example: auth user object, theme (dark/light).

3. **App-wide / Complex State (big projects)**

   * That’s when you bring in tools like:

     * **Zustand** → simple, modern, hook-based, no boilerplate.
     * **Redux Toolkit** → battle-tested, good for huge apps, still relevant.
     * **Jotai** / **Recoil** → atoms for fine-grained state control.

---

### ⚡ Example (Vite + Hooks)

Let’s say you spin up a Vite + React app:

```bash
npm create vite@latest my-app --template react
cd my-app
npm install
npm run dev
```

Basic `useState`:

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}

export default Counter;
```

If you need global state (like auth):

```jsx
import { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = (name) => setUser({ name });
  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
```

Now any component can call `useAuth()` to grab `user` or `login/logout`.

---

🔥 TL;DR:

* Start with **hooks (`useState`, `useEffect`)** for local logic.
* Use **context + reducer** for mid-level shared state.
* Pull in **Zustand/Redux** only if your app grows messy.

---

