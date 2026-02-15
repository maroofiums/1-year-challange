import { useState } from "react";
import TodoInput from "./TodoInput";
import TodoList from "./TodoList";

function App() {
  const [todos, setTodos] = useState([]);

  // Add new todo
  const addTodo = (text) => {
    if (!text) return;
    setTodos([...todos, { text, done: false }]);
  };

  // Toggle done
  const toggleDone = (index) => {
    const newTodos = [...todos];
    newTodos[index].done = !newTodos[index].done;
    setTodos(newTodos);
  };

  // Remove todo
  const removeTodo = (index) => {
    setTodos(todos.filter((_, i) => i !== index));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>My Todo App</h1>
      <TodoInput addTodo={addTodo} />
      <TodoList todos={todos} toggleDone={toggleDone} removeTodo={removeTodo} />
    </div>
  );
}

export default App;
