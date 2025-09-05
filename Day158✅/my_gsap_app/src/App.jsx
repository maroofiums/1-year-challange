import { Routes, Route } from "react-router-dom";
import TransitionLayout from "./layouts/TransitionLayout";
import Home from "./pages/Home";
import About from "./pages/About";

function App() {
  return (
    <Routes>
      <Route element={<TransitionLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Route>
    </Routes>
  );
}

export default App;
