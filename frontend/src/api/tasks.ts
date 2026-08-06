import { apiFetch, apiPatch } from "./client";
import type { TaskDetails, TaskSummary, TaskUpdate } from "../types/task";

export function getTasks(): Promise<TaskSummary[]> {
    return apiFetch<TaskSummary[]>("/tasks/");
}

export function getTaskDetails(taskId: number): Promise<TaskDetails> {
    const task_id = taskId
    return apiFetch<TaskDetails>(`/tasks/${task_id}`);
}

export function updateTask(taskId: number, formData: TaskUpdate): Promise<TaskDetails> {
    return apiPatch<TaskDetails>(`/tasks/${taskId}`, formData);
}