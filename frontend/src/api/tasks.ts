import { apiFetch } from "./client";
import type { TaskDetails2, TaskSummary } from "../types/task";

export function getTasks(): Promise<TaskSummary[]> {
    return apiFetch<TaskSummary[]>("/tasks/");
}

export function getTaskDetails(taskId: number): Promise<TaskDetails2> {
    const task_id = taskId
    return apiFetch<TaskDetails2>(`/tasks/${task_id}`);
}