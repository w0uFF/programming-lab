"use strict";
const initial = [
  { title: "Review arrays and dictionaries", done: true },
  { title: "Implement binary search", done: false },
  { title: "Write CSV import tests", done: false },
  { title: "Complete worksheet 04", done: false }
];
function readTasks() {
  try {
    const saved = JSON.parse(localStorage.getItem("practice_tasks") || "null");
    return Array.isArray(saved) ? saved : structuredClone(initial);
  } catch { return structuredClone(initial); }
}
let tasks = readTasks();
const list = document.querySelector("#tasks");
const count = document.querySelector("#count");
function render() {
  list.replaceChildren();
  for (const task of tasks) {
    const li = document.createElement("li");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.done === true;
    checkbox.addEventListener("change", () => { task.done = checkbox.checked; save(); });
    const label = document.createElement("span");
    label.textContent = String(task.title).slice(0, 80);
    if (checkbox.checked) label.className = "complete";
    li.append(checkbox, label);
    list.append(li);
  }
  count.textContent = tasks.filter(task => task.done).length + " of " + tasks.length + " complete";
}
function save() { localStorage.setItem("practice_tasks", JSON.stringify(tasks)); render(); }
document.querySelector("#add-task").addEventListener("submit", (event) => {
  event.preventDefault();
  const input = document.querySelector("#title");
  const title = input.value.trim();
  if (title) tasks.push({ title, done: false });
  input.value = "";
  save();
});
document.querySelector("#reset").addEventListener("click", () => {
  tasks = structuredClone(initial); save();
});
render();
