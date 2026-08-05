import { useState, useEffect } from "react";

import type { TaskSummary } from "../../types/task";
import { getTasks } from "../../api/tasks";
import { TaskListItem } from "./TaskListItem";

interface TaskListProps {
    onSelectTask: (taskId: number) => void;
    clickedTaskID: number | null;
}

export function TaskList({ onSelectTask, clickedTaskID }: TaskListProps) {

    const [tasks, setTasks] = useState<TaskSummary[]>([]);

    useEffect(() => {

        async function loadTasks() {

            const data = await getTasks();

            setTasks(data);

        }

        loadTasks();
    }, []);

    return (
        <main>
            <h1 className="text-2xl font-bold mb-4">
                Tasks
            </h1>

            <ul className="w-48">
                {tasks.map(task => (
                    <TaskListItem
                        task={task}
                        onSelectTask={onSelectTask}
                        isSelected={task.id === clickedTaskID}
                    />
                ))}
            </ul>
        </main>
    );
}