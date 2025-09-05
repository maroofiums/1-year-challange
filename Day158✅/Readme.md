## Day158

---

### 📂 File Structure (Vite)

```
src/
  main.jsx      
  App.jsx
  layouts/TransitionLayout.jsx
  pages/Home.jsx
  pages/About.jsx
index.html
```

---

### `index.html`

Keep it barebones:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React Router + GSAP + Vite</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

---

### `main.jsx`

This replaces `index.jsx` from CRA:

```jsx
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

---

### `App.jsx`

```jsx
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
```

---

### `layouts/TransitionLayout.jsx`

```jsx
import { useEffect, useRef } from "react";
import { Outlet, useLocation } from "react-router-dom";
import gsap from "gsap";

export default function TransitionLayout() {
  const location = useLocation();
  const container = useRef();

  useEffect(() => {
    const page = container.current;

    // Animate page entry
    gsap.fromTo(
      page,
      { opacity: 0, y: 50 },
      { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }
    );

    // Animate page exit on cleanup
    return () => {
      gsap.to(page, {
        opacity: 0,
        y: -50,
        duration: 0.5,
        ease: "power3.in"
      });
    };
  }, [location]);

  return (
    <div ref={container} className="page">
      <Outlet />
    </div>
  );
}
```

---

### `pages/Home.jsx`

```jsx
import { Link } from "react-router-dom";
import { useLayoutEffect, useRef } from "react";
import gsap from "gsap";

export default function Home() {
  const container = useRef();

  useLayoutEffect(() => {
    let ctx = gsap.context(() => {
      gsap.from(".title", { y: 100, opacity: 0, duration: 1 });
    }, container);

    return () => ctx.revert();
  }, []);

  return (
    <div ref={container} className="home">
      <h1 className="title">🏠 Home Page</h1>
      <Link to="/about">Go to About</Link>
    </div>
  );
}
```

---

### `pages/About.jsx`

```jsx
import { Link } from "react-router-dom";
import { useLayoutEffect, useRef } from "react";
import gsap from "gsap";

export default function About() {
  const container = useRef();

  useLayoutEffect(() => {
    let ctx = gsap.context(() => {
      gsap.from(".title", { x: -100, opacity: 0, duration: 1 });
    }, container);

    return () => ctx.revert();
  }, []);

  return (
    <div ref={container} className="about">
      <h1 className="title">ℹ️ About Page</h1>
      <Link to="/">Back Home</Link>
    </div>
  );
}
```

---

### 🚀 Run It

1. Install deps:

   ```sh
   npm install react-router-dom gsap
   ```
2. Start dev server:

   ```sh
   npm run dev
   ```
3. Open `http://localhost:5173` → you’ll see animated route transitions working.

---
