import React, { createContext, useContext, useReducer, useMemo, useCallback } from "react";
import TodoList from "./TodoList";
import useFetch from "./useFetch";

// ---------------- Context Setup ----------------
const ThemeContext = createContext();

const themeReducer = (state, action) => {
  switch (action.type) {
    case "TOGGLE_THEME":
      return state === "light" ? "dark" : "light";
    default:
      return state;
  }
};

// ---------------- Main App ----------------
export default function App() {
  const [theme, dispatch] = useReducer(themeReducer, "light");

  // Using custom hook to fetch data
  const data = useFetch("https://jsonplaceholder.typicode.com/users");

  const themeStyles = useMemo(() => ({
    backgroundColor: theme === "light" ? "#fff" : "#333",
    color: theme === "light" ? "#000" : "#fff",
    minHeight: "100vh",
    padding: "20px",
    transition: "0.3s"
  }), [theme]);

  const toggleTheme = useCallback(() => {
    dispatch({ type: "TOGGLE_THEME" });
  }, []);

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div style={themeStyles}>
        <h1>React Hooks & Advanced State Management</h1>
        <button onClick={toggleTheme}>
          Toggle Theme ({theme})
        </button>
        
        <hr />

        <h2>Users (from API)</h2>
        {data ? (
          <ul>
            {data.map(user => <li key={user.id}>{user.name}</li>)}
          </ul>
        ) : (
          <p>Loading...</p>
        )}

        <hr />

        <TodoList />
      </div>
    </ThemeContext.Provider>
  );
}

// ---------------- Custom Hook to use Theme ----------------
export const useTheme = () => useContext(ThemeContext);
