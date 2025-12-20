gsap.registerPlugin(ScrollTrigger);

let tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".product",
    start: "top top",
    end: "bottom bottom",
    scrub: 1,
    pin: true,
  }
});

tl.fromTo(".product-image img",
  { scale: 0.6, rotate: -20, opacity: 0 },
  { scale: 1, rotate: 0, opacity: 1, duration: 2, ease: "power2.out" }
)
.fromTo(".product-title",
  { y: 100, opacity: 0 },
  { y: 0, opacity: 1, duration: 1 },
  "-=1"
)
.fromTo(".product-desc",
  { y: 100, opacity: 0 },
  { y: 0, opacity: 1, duration: 1 },
  "-=0.8"
)
.to(".product-image img",
  { scale: 1.3, rotate: 15, opacity: 0.5, duration: 2 },
  "+=1"
);
const words = ["Creative", "Dynamic", "Smooth", "Powerful"];
let currentWord = 0;
const morphText = document.querySelector(".morph-text");

function changeWord() {
  gsap.to(morphText, {
    duration: 0.5,
    opacity: 0,
    y: -30,
    ease: "power2.inOut",
    onComplete: () => {
      currentWord = (currentWord + 1) % words.length;
      morphText.textContent = words[currentWord];
      gsap.fromTo(morphText,
        { opacity: 0, y: 30 },
        { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }
      );
    },
  });
}

setInterval(changeWord, 2000);
