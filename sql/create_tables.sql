CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year INT NOT NULL
);

CREATE TABLE sequences(
    id SERIAL PRIMARY KEY,
    seq_code VARCHAR(20) UNIQUE NOT NULL,
    movie_id INT 
        REFERENCES movies(id) 
        ON DELETE RESTRICT
);

CREATE TABLE shots(

    id SERIAL PRIMARY KEY,
    shot_code VARCHAR(20) UNIQUE NOT NULL,
    frame_start INT DEFAULT 1001,
    frame_end INT DEFAULT 1101,
    sequence_id INT 
        REFERENCES sequences(id) 
        ON DELETE RESTRICT
);

CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    department_id INT NOT NULL
        REFERENCES departments(id)
        ON DELETE RESTRICT
);

CREATE TABLE task_statuses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE task_priorities(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    shot_id INT NOT NULL
        REFERENCES shots(id)
        ON DELETE RESTRICT,
    task_type_id INT NOT NULL
        REFERENCES task_type_id,
    artist_id INT NOT NULL
        REFERENCES artists(id)
        ON DELETE RESTRICT,
    status_id INT NOT NULL
        REFERENCES task_statuses(id)
        ON DELETE RESTRICT,
    start_date DATE DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    priority_id INT 
        REFERENCES task_priorities(id),
    task_note TEXT
);
