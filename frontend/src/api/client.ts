const API_BASE_URL = "http://localhost:8000";

export async function apiFetch<T>(path: string): Promise<T> {
    const response = await fetch(`${API_BASE_URL}${path}`);

    if (!response.ok) {
        throw new Error("Failed to fetch data");
    }

    return response.json();
}