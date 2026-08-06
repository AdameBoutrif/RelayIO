import { apiFetch } from "./client";
import type { TaskPriorities } from "../types/taskPriority";

export function getArtists(): Promise<TaskPriorities[]> {
    return apiFetch<TaskPriorities[]>("/task_priorities/");
}