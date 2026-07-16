INSERT INTO departments (name)
VALUES
('Layout'),
('Animation'),
('Lighting'),
('FX'),
('Compositing'),
('Grade'),
('Editorial');

INSERT INTO task_statuses (name)
VALUES
('Ready'),
('In Progress'),
('Review'),
('Approved'),
('Final');

INSERT INTO task_priorities (name)
VALUES
('Low'),
('Medium'),
('High'),
('Critical');


INSERT INTO task_types (name)
VALUES
('Animation'),
('Lighting'),
('FX'),
('Compositing'),
('Matchmove'),
('Layout');

INSERT INTO movies (title, release_year)
VALUES
('Project Atlas', 2027),
('The Last Signal', 2028);

INSERT INTO sequences (sequence_code, movie_id)
VALUES
('PA010', 1),
('PA020', 1),
('PA030', 1),
('PA040', 1),
('TLS010', 2),
('TLS020', 2),
('TLS030', 2),
('TLS040', 2);

INSERT INTO shots (shot_code, sequence_id)
VALUES
('SH010', 1),
('SH020', 1),
('SH030', 1),
('SH040', 1),
('SH015', 2),
('SH020', 2),
('SH050', 3),
('SH005', 4),
('SH012', 4),
('SH033', 5),
('SH010', 6),
('SH140', 7),
('SH010', 8);

INSERT INTO artists (first_name, last_name, email, department_id)
VALUES
('Bob', 'Dylan', 'bob.dylan@gmail.com', 3),
('Bugzy', 'Malone', 'b.malone@gmail.com', 7),
('Franz', 'Reynolds', 'magnumf@gmail.com', 1),
('David', 'Mura', 'd.muraw@gmail.com', 2),
('Ashley', 'Lib', 'ashlib@hotmail.com', 4),
('Sarah', 'Stone', 'sarahi@gmail.com', 5),
('Kumar', 'Nanj', 'bigk@gmail.com', 6);

