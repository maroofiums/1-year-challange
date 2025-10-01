import { useReducer, useState } from "react";

const reducer = (state, action) => {
  switch (action.type) {
    case "add":
      return [...state, { text: action.payload, id: Date.now() }];
    case "delete":
      return state.filter((item) => item.id !== action.payload);
    default:
      return state;
  }
};

export default function ReducerTodo() {
  const [todos, dispatch] = useReducer(reducer, []);
  const [input, setInput] = useState("");

  return (
    <div className="my-6">
      <input
        type="text"
        className="border p-2"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        onClick={() => {
          dispatch({ type: "add", payload: input });
          setInput("");
        }}
        className="ml-2 px-4 py-2 bg-purple-600 text-white"
      >
        Add Todo
      </button>

      <ul className="mt-4">
        {todos.map((todo) => (
          <li key={todo.id} className="flex justify-between w-64">
            {todo.text}
            <button onClick={() => dispatch({ type: "delete", payload: todo.id })} className="text-red-600">
              ✖
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
