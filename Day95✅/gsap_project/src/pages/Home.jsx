// src/pages/Home.jsx
import { useEffect, useRef } from "react";
import gsap from "gsap";

const Home = () => {
  const box = useRef();

  useEffect(() => {
    console.log("🏠 Home component mounted");
    if (box.current) {
      gsap.from(box.current, {
        opacity: 0,
        y: 50,
        duration: 1,
        ease: "power3.out",
      });
    }
  }, []);

  return (
    <div className="page">
      <div ref={box}>
        <h1>🏠 Home Page</h1>
        <p>This is the homepage animated by GSAP.</p>
      </div>
    </div>
  );
};

export default Home;
