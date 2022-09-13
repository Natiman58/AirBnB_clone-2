-- Creates a database named hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a user at local host and grant all permissions on this db
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant SELECT privilege on the databse performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
