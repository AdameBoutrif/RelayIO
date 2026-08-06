import { Button } from "../ui/Button"
import type { TaskDetails } from "../../types/task";
import { useState } from "react";

import type { TaskUpdate } from "../../types/task";
import { FormTextArea } from "../ui/FormTextArea";

interface TaskFormProps {
    task: TaskDetails;
    onSave: (task_id: number, formData: TaskUpdate) => void;
    onCancel: () => void;
}

export function TaskForm({ task, onCancel, onSave }: TaskFormProps) {

    const [formData, setFormData] = useState<TaskUpdate>({
        artist_id: task.artist.id,
        shot_id: task.shot.id,
        task_type_id: task.task_type.id,
        status_id: task.task_status.id,
        priority_id: task.priority.id,
        start_date: task.start_date,
        due_date: task.due_date,
        task_note: task.task_note ?? '',
    });

    const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement | HTMLInputElement>) => {
        const { name, value } = e.target;

        setFormData((prev) => {

            const udpatedState = {
                ...prev,
                [name]: value,
            };

            return udpatedState;
        });
    }


    if (task === null) {
        return (
            <div>Error, there is no task selected!</div>
        );
    }

    return (
        <div>
            <div>
                <div>
                    TASK FORM
                </div>
                <div className="flex">
                    <p>Artist:</p><p> {task?.artist.full_name}</p>
                </div>
                <div className="flex">
                    <FormTextArea
                        label="Task Note:"
                        name="task_note"
                        value={formData.task_note}
                        onChange={handleInputChange}
                    />
                </div>

                <div className="flex">
                    <Button name="Save" onClick={() => onSave(task.id, formData)} />
                    <Button name="Cancel" onClick={onCancel} />
                </div>

            </div>
        </div>
    );
}