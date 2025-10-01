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
