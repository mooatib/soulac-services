insert into user (id, username, email, password) values (1, 'dib','dib@gmail.com', '$2b$12$veVnC5I83mQ0q73s9B3W9erJbMYDd.Z89UvT90bOV8gGhLsrLB0OC');
insert into soulacais (id, uid, img, sex, weight, resistance, alcohol, trend) values (1, 1, 'https://img.freepik.com/vecteurs-libre/personnage-avatar-jeune-homme_24877-36969.jpg', 1, 62, 2, 1.0, 'ASC');
insert into `group` (id, name, description, private) values (1, 'Soulac Official', 'THE BEST PLACE TO BE', 1);
insert into soulacais_groups (soulacais_id, group_id, role) values (1, 1, 'admin');
insert into alcohol(id, name, type, percentage, hidden) values (1, 'Chouffe', 0, 8.0, 0);
insert into drink (id, sid, aid, quantity, date) values (1, 1, 1, 50, CURDATE());
insert into drink (id, sid, aid, quantity, date) values (2, 1, 1, 50, CURDATE());
insert into drink (id, sid, aid, quantity, date) values (3, 1, 1, 50, CURDATE());