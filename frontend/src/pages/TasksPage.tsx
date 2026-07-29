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
                        <p><strong>Shot:</strong> {task.shot}</p>
                        <p><strong>Artist:</strong> {task.artist}</p>
                        <p><strong>Task Type:</strong> {task.task_type}</p>
                        <p><strong>Status:</strong> {task.status}</p>
                        <p><strong>Priority:</strong> {task.priority}</p>
                        <p><strong>Due Date:</strong> {task.due_date}</p>
                    </li>
                ))}
            </ul>
        </main>
    );
}