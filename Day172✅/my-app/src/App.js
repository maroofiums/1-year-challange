import { Routes, Route, useLocation, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

import PageTransition from "./PageTransition";
import TransitionOverlay from "./TransitionOverlay";
import Navbar from "./Navbar";

import Home from "./pages/Home";
import About from "./pages/About";

export default function App() {
  const location = useLocation();
  const navigate = useNavigate();

  const [nextPath, setNextPath] = useState(null);

  // navigate AFTER overlay animation
  useEffect(() => {
    if (nextPath) {
      const timeout = setTimeout(() => {
        navigate(nextPath);
        setNextPath(null);
      }, 1000); // matches TransitionOverlay duration
      return () => clearTimeout(timeout);
    }
  }, [nextPath, navigate]);

  return (
    <>
      <Navbar setNextPath={setNextPath} />
      {nextPath && <TransitionOverlay />}

      <Routes location={location} key={location.pathname}>
        <Route
          path="/"
          element={
            <PageTransition>
              <Home />
            </PageTransition>
          }
        />
        <Route
          path="/about"
          element={
            <PageTransition>
              <About />
            </PageTransition>
          }
        />
      </Routes>
    </>
  );
}
