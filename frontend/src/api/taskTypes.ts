import { apiFetch } from "./client";
import type { TaskTypes } from "../types/taskType";

export function getArtists(): Promise<TaskTypes[]> {
    return apiFetch<TaskTypes[]>("/task_types/");
}