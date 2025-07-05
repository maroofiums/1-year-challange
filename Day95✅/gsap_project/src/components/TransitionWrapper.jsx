// components/TransitionWrapper.jsx
import { useEffect, useRef } from "react";
import gsap from "gsap";

const TransitionWrapper = ({ children }) => {
  const wrapper = useRef();

  useEffect(() => {
    gsap.fromTo(
      wrapper.current,
      { opacity: 0, y: 30 },
      { opacity: 1, y: 0, duration: 1 }
    );
  }, []);

  return <div ref={wrapper}>{children}</div>;
};

export default TransitionWrapper;
