import type { TaskSummary } from "../../types/task";

interface TaskListItemProps {
    task: TaskSummary;
    onSelectTask: (taskId: number) => void;
}

export function TaskListItem({ task, onSelectTask }: TaskListItemProps) {
    return (
        <div onClick={() => onSelectTask(task.id)}
            className="rounded-lg border border-slate-300 p-4 hover:bg-slate-50 cursor-pointer">
            <div>
                Task ID: {task.id}
            </div>

            <div className="flex gap-2">
                <span className="font-semibold">
                    {task.shot}
                </span>
                <span className="font-semibold">
                    {task.task_type}
                </span>
            </div>

            <p>
                {task.artist}
            </p>

            <p className="text-sm text-slate-600">
                {task.status}
            </p>
        </div>
    );
}