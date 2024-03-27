-- create the MYSQL server User user_0d_1
-- should have all privileges
-- set password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL privileges ON *.* TO 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
