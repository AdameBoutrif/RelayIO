import { useEffect, useState } from "react";
import type { TaskDetails } from "../../types/task";
import { getTaskDetails, updateTask } from "../../api/tasks";
import { TaskDetailsItem } from "./TaskDetailsItem";
import { Button } from "../ui/Button";
import { TaskForm } from "./TaskForm";

interface TaskDetailsProps {
    taskId: number | null;
}

export function TaskDetails({ taskId }: TaskDetailsProps) {

    const [task, setTask] = useState<TaskDetails | null>(null);

    const [isEditing, setIsEditing] = useState(false);


    useEffect(() => {

        if (taskId === null) {
            return;
        };


        const id = taskId;

        async function loadTaskDetails() {

            setTask(null);

            const data = await getTaskDetails(id);

            setTask(data);

        }

        loadTaskDetails();

    }, [taskId]);

    if (taskId === null) {
        return (
            <section>
                <h2 className="text-xl font-semibold">
                    Task Details
                </h2>

                <p>
                    Select a task to view its details.
                </p>
            </section>
        );
    }

    if (task === null) {
        return (
            <section>
                <h2 className="text-xl font-semibold">
                    Task Details
                </h2>

                <p>
                    Task Loading...
                </p>
            </section>
        );
    }

    if (isEditing) {
        return (
            <div>
                <TaskForm
                    task={task}
                    onCancel={() => setIsEditing(false)}
                    onSave={async (id, data) => {

                        const updatedTask = await updateTask(id, data);

                        setTask(updatedTask);

                        setIsEditing(false);

                    }}
                />
            </div>
        );
    }

    return (
        <section>

            <div>
                <p className="text-xl font-semibold">
                    Task Details
                </p>
            </div>

            <div>
                <TaskDetailsItem label="Task ID" value={task.id} />
                <TaskDetailsItem label="Artist" value={task.artist.full_name} />
                <TaskDetailsItem label="Shot Code" value={task.shot.shot_code} />
                <TaskDetailsItem label="Task Type" value={task.task_type.name} />
                <TaskDetailsItem label="Task Status" value={task.task_status.name} />
                <TaskDetailsItem label="Start Date" value={task.start_date} />
                <TaskDetailsItem label="Due Date" value={task.due_date} />
                <TaskDetailsItem label="Priority" value={task.priority.name} />
                <TaskDetailsItem label="Notes" value={task.task_note} />
            </div>
            <p className="text-l font-semibold">
                Options:
            </p>
            <Button
                name="Edit"
                onClick={() => setIsEditing(true)} />

        </section >
    );
}