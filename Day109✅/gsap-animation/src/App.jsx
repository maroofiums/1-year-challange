import { Routes, Route, useLocation } from 'react-router-dom';
import { useLayoutEffect } from 'react';
import gsap from 'gsap';

import Home from './pages/Home';
import About from './pages/About';

function App() {
  const location = useLocation();

  useLayoutEffect(() => {
    const tl = gsap.timeline();

    tl.to(".page", { opacity: 0, y: 50, duration: 0.5 })
      .set(".page", { y: -50 })
      .to(".page", { opacity: 1, y: 0, duration: 0.5 });
  }, [location.pathname]);

  return (
    <Routes location={location} key={location.pathname}>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
    </Routes>
  );
}

export default App;
