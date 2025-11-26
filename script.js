let tasks = [];

function addTask() {
    const title = document.getElementById("title").value;
    const urgency = document.getElementById("urgency").value;
    const importance = document.getElementById("importance").value;
    const effort = document.getElementById("effort").value;

    if (!title) return alert("Enter a task title!");

    tasks.push({
        title: title,
        urgency: urgency,
        importance: importance,
        effort: effort
    });

    document.getElementById("taskList").innerHTML += `<li>${title}</li>`;
}

async function analyze() {
    const response = await fetch("http://127.0.0.1:8000/api/analyze/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ tasks: tasks })
    });

    const data = await response.json();

    document.getElementById("results").textContent =
        JSON.stringify(data.results, null, 2);
}
