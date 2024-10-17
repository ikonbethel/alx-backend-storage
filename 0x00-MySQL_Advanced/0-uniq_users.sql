-- Task 0: We are all unique!
-- Creates a table users following these requirements:
-- With these attributes:
--	id, integer, never null, auto increment and primary key
--	email, string (255 characters), never null and unique
--	name, string (255 characters)
-- If the table already exists, script should not fail

CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
);
