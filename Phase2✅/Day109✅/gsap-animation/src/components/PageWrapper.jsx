import { useRef, useEffect } from 'react';
import gsap from 'gsap';

export default function PageWrapper({ children }) {
  const ref = useRef();

  useEffect(() => {
    gsap.fromTo(
      ref.current,
      { opacity: 0, y: 40 },
      { opacity: 1, y: 0, duration: 0.8, ease: 'power2.out' }
    );
  }, []);

  return <div ref={ref} className="page">{children}</div>;
}
