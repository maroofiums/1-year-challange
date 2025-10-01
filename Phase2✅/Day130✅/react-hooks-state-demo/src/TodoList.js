import React, { useState, useReducer } from "react";
import { useTheme } from "./App";

// Reducer for todo state
const todoReducer = (state, action) => {
  switch (action.type) {
    case "ADD_TODO":
      return [...state, { id: Date.now(), text: action.payload, completed: false }];
    case "TOGGLE_TODO":
      return state.map(todo =>
        todo.id === action.payload ? { ...todo, completed: !todo.completed } : todo
      );
    case "DELETE_TODO":
      return state.filter(todo => todo.id !== action.payload);
    default:
      return state;
  }
};

export default function TodoList() {
  const [input, setInput] = useState("");
  const [todos, dispatch] = useReducer(todoReducer, []);
  const { theme } = useTheme();

  const handleAdd = () => {
    if (input.trim()) {
      dispatch({ type: "ADD_TODO", payload: input });
      setInput("");
    }
  };

  return (
    <div>
      <h2>Todo List ({theme} mode)</h2>
      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Add a task"
      />
      <button onClick={handleAdd}>Add</button>

      <ul>
        {todos.map(todo => (
          <li
            key={todo.id}
            style={{
              textDecoration: todo.completed ? "line-through" : "none",
              cursor: "pointer"
            }}
            onClick={() => dispatch({ type: "TOGGLE_TODO", payload: todo.id })}
          >
            {todo.text}
            <button
              style={{ marginLeft: "10px" }}
              onClick={(e) => {
                e.stopPropagation();
                dispatch({ type: "DELETE_TODO", payload: todo.id });
              }}
            >
              ❌
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
