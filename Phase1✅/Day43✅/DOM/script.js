// Selecting Elements
const title = document.getElementById("title");
const description = document.querySelector(".description");
const itemList = document.getElementById("itemList");
const addItemBtn = document.getElementById("addItemBtn");
const toggleListBtn = document.getElementById("toggleListBtn");
const newItemInput = document.getElementById("newItemInput");
const changeTitleBtn = document.getElementById("changeTitleBtn");

// Event Listener to Add Item
addItemBtn.addEventListener("click", () => {
  const newItemText = newItemInput.value.trim();
  if (newItemText !== "") {
    const li = document.createElement("li");
    li.className = "item";
    li.innerHTML = `${newItemText} <button class="removeBtn">Remove</button>`;
    itemList.appendChild(li);
    newItemInput.value = "";
  }
});

// Event Delegation: Remove Items
itemList.addEventListener("click", (e) => {
  if (e.target.classList.contains("removeBtn")) {
    const li = e.target.parentElement;
    li.remove();
  }
});

// Toggle List Visibility
toggleListBtn.addEventListener("click", () => {
  itemList.classList.toggle("hidden");
});

// Change Title Text and Style
changeTitleBtn.addEventListener("click", () => {
  title.textContent = "DOM Mastered!";
  title.style.color = "green";
  title.classList.toggle("highlight");
});

// Attribute Manipulation
title.setAttribute("data-info", "Main heading");
console.log(title.getAttribute("data-info"));

// DOM Traversal Example
console.log("Parent of itemList:", itemList.parentElement);
console.log("First child:", itemList.firstElementChild);
console.log("Last child:", itemList.lastElementChild);

// Class Manipulation
description.classList.add("highlight");
setTimeout(() => {
  description.classList.remove("highlight");
}, 2000);
