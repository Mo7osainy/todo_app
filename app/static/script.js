const apiUrl = "/api/tasks";
const taskList = document.getElementById("taskList");
const addBtn = document.getElementById("addBtn");
const taskInput = document.getElementById("taskInput");
const taskCount = document.getElementById("taskCount");
const showTasksBtn = document.getElementById("showTasksBtn");

let currentTasks = [];

// تحميل عدد المهام فقط
async function loadTaskCount() {
    const res = await fetch(apiUrl);
    currentTasks = await res.json();
    taskCount.textContent = `You have ${currentTasks.length} task${currentTasks.length !== 1 ? 's' : ''}.`;
    taskList.innerHTML = ""; // مسح أي عرض قديم
}

// تحميل المهام كاملة عند الضغط على الزر
function renderTasks() {
    taskList.innerHTML = "";
    currentTasks.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `
            <span>${task.title}</span>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(li);
    });
}

async function addTask() {
    const title = taskInput.value.trim();
    if (!title) return alert("Please enter a task first!");
    await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title })
    });
    taskInput.value = "";
    await loadTaskCount(); // تحديث العدد بعد إضافة مهمة
}

async function deleteTask(id) {
    await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
    await loadTaskCount(); // تحديث العدد بعد الحذف
    renderTasks(); // إعادة عرض المهام لو كانت ظاهرة
}

showTasksBtn.addEventListener("click", renderTasks);
addBtn.addEventListener("click", addTask);

document.addEventListener("DOMContentLoaded", loadTaskCount);

