export interface TaskSummary {
    id: number;
    shot: string;
    artist: string;
    task_type: string;
    status: string;
    priority: string;
    due_date: string;
}

export interface TaskDetails_old {
    id: number;
    start_date: string;
    due_date: string;
    task_note: string;

    artist: string;
    shot: string;
    task_type: string;
    task_status: string;
    priority: string;
}

export interface TaskDetails {
    id: number;

    start_date: string;
    due_date: string;
    task_note: string;

    artist: {
        id: number;
        full_name: string;
    };

    shot: {
        id: number;
        shot_code: string;
    };

    task_type: {
        id: number;
        name: string;
    };

    task_status: {
        id: number;
        name: string;
    };

    priority: {
        id: number;
        name: string;
    };
}

export interface TaskUpdate {
    artist_id: number;
    shot_id: number;
    task_type_id: number;
    status_id: number;
    priority_id: number;

    start_date: string;
    due_date: string;
    task_note: string;
}

