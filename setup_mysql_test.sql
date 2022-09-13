-- create db hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create user 
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

-- set pwd for user
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';

-- grant the user  all previleges on db 'hbnb_test_db'
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';

-- grant the user only SELECT previlege on db 'performance_schema'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- grant the user all access on the db 'hbnb_test_db'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- comit changes
FLUSH PRIVILEGES;
