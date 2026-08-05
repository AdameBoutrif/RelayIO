import type { TaskSummary } from "../../types/task";

interface TaskListItemProps {
    task: TaskSummary;
    onSelectTask: (taskId: number) => void;

    isSelected: boolean;
}

export function TaskListItem({ task, onSelectTask, isSelected }: TaskListItemProps) {
    return (
        <div>
            <div onClick={() => onSelectTask(task.id)}
                className={`
                            "w-32 h-32 rounded-xl 
                            border 
                            p-4 
                            cursor-pointer
                            ${isSelected
                        ? "bg-white/75 border-white-90"
                        : "bg-white/30 hover:bg-white/75"
                    }
                    `}>
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
        </div>
    );
}