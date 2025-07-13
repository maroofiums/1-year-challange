import Counter from "./components/Counter";
import Quote from "./components/Quote";
import ThemeToggler from "./components/ThemeToggler";
import { ThemeProvider } from "./components/ThemeContext";
import ReducerTodo from "./components/ReducerTodo";

export default function App() {
  return (
    <ThemeProvider>
      <div className="p-6 max-w-lg mx-auto">
        <h1 className="text-3xl font-bold mb-4">React Hooks Playground</h1>
        <ThemeToggler />
        <Counter />
        <Quote />
        <ReducerTodo />
      </div>
    </ThemeProvider>
  );
}
