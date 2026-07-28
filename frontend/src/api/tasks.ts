import { apiFetch } from "./client";
import type { Task } from "../types/task";

export function getTasks(): Promise<Task[]> {
    return apiFetch<Task[]>("/tasks");
    console.log("Fetching Data");
}