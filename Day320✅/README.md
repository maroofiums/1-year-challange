# Day 320


# **Step 0: Setup**

1. Node.js installed ho aur terminal ready ho
2. Naya React project create karo (Vite recommended)

```bash
npm create vite@latest my-todo-app
cd my-todo-app
npm install
npm run dev
```

* Browser kholke `http://localhost:5173/` dekho → blank React page

---

# **Step 1: App Structure**

Simple structure:

```
src/
 ├─ App.jsx        // main component
 ├─ TodoInput.jsx  // input + add button
 └─ TodoList.jsx   // list of todos
```

---

# **Step 2: App.jsx (Parent Component)**

```jsx
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
```

* `todos` state me task objects stored hain `{text, done}`
* Functions: **addTodo, toggleDone, removeTodo**
* Components ko functions props ke through pass kiye

---

# **Step 3: TodoInput.jsx (Input Component)**

```jsx
import { useState } from "react";

function TodoInput({ addTodo }) {
  const [text, setText] = useState("");

  const handleAdd = () => {
    addTodo(text);
    setText(""); // input clear
  };

  return (
    <div>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add a task"
      />
      <button onClick={handleAdd}>Add</button>
    </div>
  );
}

export default TodoInput;
```

* **useState** → input value track karne ke liye
* **onChange** → input ke text ko update karne ke liye
* **onClick** → addTodo function call

---

# **Step 4: TodoList.jsx (Display Todos)**

```jsx
function TodoList({ todos, toggleDone, removeTodo }) {
  if (todos.length === 0) return <p>No tasks yet!</p>;

  return (
    <ul>
      {todos.map((todo, index) => (
        <li key={index} style={{ marginBottom: "10px" }}>
          <span style={{ textDecoration: todo.done ? "line-through" : "none" }}>
            {todo.text}
          </span>
          <button onClick={() => toggleDone(index)} style={{ marginLeft: "10px" }}>
            Toggle
          </button>
          <button onClick={() => removeTodo(index)} style={{ marginLeft: "5px" }}>
            Remove
          </button>
        </li>
      ))}
    </ul>
  );
}

export default TodoList;
```

* List me **todos.map()** use kiya
* `key` prop zaruri hai React ko list track karne ke liye
* Conditional rendering → `line-through` agar task done ho

---

# **Step 5: Run & Test**

```bash
npm run dev
```

Browser me:

* Task add karna
* Toggle (complete/incomplete)
* Remove task

Everything should work. ✅
---

# **Key Concepts Covered**

* Components → App, TodoInput, TodoList
* Props → Parent → Child
* State → Dynamic data management
* Event handling → onClick, onChange
* Conditional rendering → line-through
* Lists & keys → todos.map()