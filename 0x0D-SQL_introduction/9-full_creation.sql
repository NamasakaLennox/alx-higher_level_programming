-- Creates a table second table if it doesn't exit and add multiple rows
-- create table
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- insert value 1
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
-- insert value 2
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
-- insert value 3
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
-- insert value 4
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
