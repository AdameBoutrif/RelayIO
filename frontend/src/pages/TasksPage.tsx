import { useState, useEffect } from "react";

import type { Task } from "../types/task";
import { getTasks } from "../api/tasks";



export function TasksPage() {
    const [tasks, setTasks] = useState<Task[]>([]);

    useEffect(() => {
        console.log("useEffect is running");

        async function loadTasks() {
            console.log("Calling getTasks()");

            const data = await getTasks();

            console.log(data);

            setTasks(data);

        }

        loadTasks();
    }, []);

    return (
        <main>
            <h1 className="text-2xl font-bold mb-4">
                Tasks
            </h1>

            <ul>
                {tasks.map(task => (
                    <li
                        key={task.id}
                        className="rounded-md border border-slate-300 p-4"
                    >
                        <p><strong>ID:</strong> {task.id}</p>
                        <p><strong>Shot:</strong> {task.shot_id}</p>
                        <p><strong>Artist:</strong> {task.artist_id}</p>
                        <p><strong>Status:</strong> {task.status_id}</p>
                        <p><strong>Start Date:</strong> {task.start_date}</p>
                        <p><strong>Due Date:</strong> {task.due_date}</p>
                        <p><strong>Priority:</strong> {task.priority_id}</p>
                        <p><strong>Note:</strong> {task.task_note}</p>
                    </li>
                ))}
            </ul>
        </main>
    );
}