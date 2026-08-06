import type { TaskUpdate } from "../types/task";

const API_BASE_URL = "http://localhost:8000";

export async function apiFetch<T>(path: string): Promise<T> {
    const response = await fetch(`${API_BASE_URL}${path}`);

    if (!response.ok) {
        throw new Error("Failed to fetch data");
    }

    return response.json();
}

export async function apiPatch<T>(path: string, body: unknown): Promise<T> {
    const response = await fetch(`${API_BASE_URL}${path}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(body)
    });

    if (!response.ok) {
        throw new Error("Failed to patch data");
    }

    return response.json();
}