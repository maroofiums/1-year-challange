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

