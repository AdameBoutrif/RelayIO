export interface Task {
    id: number;
    shot_id: number;
    task_type_id: number;
    artist_id: number;
    status_id: number;
    start_date: string;
    due_date: string;
    priority_id: number;
    task_note: string | null;
}