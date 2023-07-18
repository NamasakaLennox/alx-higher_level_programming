-- Converts the database to UTF8
-- convert the database to utf8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-- switch to database
USE hbtn_0c_0;
-- convert the table to utf8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
