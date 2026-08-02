import { useEffect, useState } from "react";
import type { TaskDetails2 } from "../../types/task";
import { getTaskDetails } from "../../api/tasks";

interface TaskDetailsProps {
    taskId: number | null;
}

export function TaskDetails({ taskId }: TaskDetailsProps) {

    const [task, setTask] = useState<TaskDetails2 | null>(null);

    useEffect(() => {

        if (taskId === null) {
            return;
        };

        const id = taskId;

        async function loadTaskDetails() {

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
                    Select a task to view it's details.
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

    return (
        <section>
            <h2 className="text-xl font-semibold">
                Task Details
            </h2>

            <p className="flex flex-col">
                <strong>Artist:</strong>{task.artist.full_name}
                <strong>Shot Code: </strong>{task.shot.shot_code}
                <strong>Task Type: </strong>{task.task_type.name}
                <strong>Task Status: </strong>{task.task_status.name}
                <strong>Start Date: </strong>{task.start_date}
                <strong>Due Date: </strong>{task.due_date}
                <strong>Priority: </strong>{task.priority.name}
                <strong>Notes: </strong>{task.task_note}
            </p>

        </section>
    );
}