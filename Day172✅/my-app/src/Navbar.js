export default function Navbar({ setNextPath }) {
  return (
    <nav style={{ padding: "10px", background: "#222", color: "#fff" }}>
      <button
        style={{ marginRight: "10px" }}
        onClick={() => setNextPath("/")}
      >
        Home
      </button>
      <button onClick={() => setNextPath("/about")}>About</button>
    </nav>
  );
}
