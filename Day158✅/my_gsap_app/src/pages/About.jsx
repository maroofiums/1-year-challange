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
