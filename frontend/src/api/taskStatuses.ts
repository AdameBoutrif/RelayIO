import { apiFetch } from "./client";
import type { TaskStatuses } from "../types/taskStatus";

export function getArtists(): Promise<TaskStatuses[]> {
    return apiFetch<TaskStatuses[]>("/task_statuses/");
}