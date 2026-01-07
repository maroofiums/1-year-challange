const btn = document.getElementById("loadBtn");

btn.addEventListener("click", () => {
  btn.innerText = "Loading...";
  btn.classList.add("loading");

  setTimeout(() => {
    btn.innerText = "Done ✔";
    btn.classList.remove("loading");
  }, 2000);
});
