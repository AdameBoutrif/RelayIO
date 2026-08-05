import { Button } from "../ui/Button"
import type { TaskDetails } from "../../types/task";

interface TaskFormProps {
    task?: TaskDetails | null;
    onCancel: () => void;
}

export function TaskForm({ task, onCancel }: TaskFormProps) {
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
                <div>{task?.artist.full_name}</div>
                <div>
                    DROP DOWN
                </div>

                <div className="flex">
                    <Button name="Save" />
                    <Button name="Cancel" onClick={onCancel} />
                </div>

            </div>
        </div>
    );
}