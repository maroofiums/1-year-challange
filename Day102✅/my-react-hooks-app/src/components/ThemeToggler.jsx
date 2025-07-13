import { useContext } from "react";
import { ThemeContext } from "./ThemeContext";

export default function ThemeToggler() {
  const { theme, toggle } = useContext(ThemeContext);

  return (
    <div className="my-4">
      <p>Current Theme: {theme}</p>
      <button onClick={toggle} className="px-4 py-2 bg-blue-600 text-white">
        Toggle Theme
      </button>
    </div>
  );
}
