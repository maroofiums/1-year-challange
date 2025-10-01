import React from "react";
import { useGlobal } from "./state/GlobalState";

function App() {
  const { state, dispatch } = useGlobal();

  return (
    <div
      style={{
        background: state.theme === "light" ? "#fff" : "#222",
        color: state.theme === "light" ? "#000" : "#fff",
        minHeight: "100vh",
        padding: "2rem",
      }}
    >
      <h1>🚀 Global State Demo</h1>

      <p>Current Theme: {state.theme}</p>
      <button onClick={() => dispatch({ type: "TOGGLE_THEME" })}>
        Toggle Theme
      </button>

      <hr />

      {state.user ? (
        <>
          <p>Welcome, {state.user.name}!</p>
          <button onClick={() => dispatch({ type: "LOGOUT" })}>Logout</button>
        </>
      ) : (
        <button
          onClick={() =>
            dispatch({ type: "LOGIN", payload: { name: "Maroof" } })
          }
        >
          Login as Maroof
        </button>
      )}
    </div>
  );
}

export default App;
