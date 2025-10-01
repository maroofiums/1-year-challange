import { useRef } from "react";
import { gsap } from "gsap";
import { useGSAP } from "@gsap/react";

export default function TransitionOverlay() {
  const overlayRef = useRef();

  useGSAP(() => {
    const tl = gsap.timeline();

    tl.fromTo(
      overlayRef.current,
      { scaleX: 0 },
      {
        scaleX: 1,
        duration: 0.5,
        transformOrigin: "left center",
        ease: "power2.inOut",
      }
    ).to(overlayRef.current, {
      scaleX: 0,
      duration: 0.5,
      transformOrigin: "right center",
      ease: "power2.inOut",
      delay: 0.2,
    });
  }, { scope: overlayRef });

  return (
    <div
      ref={overlayRef}
      style={{
        position: "fixed",
        inset: 0,
        background: "#111",
        zIndex: 9999,
      }}
    />
  );
}
