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
