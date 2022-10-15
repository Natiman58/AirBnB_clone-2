-- Creates a database named hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user named 'hbnb_dev_db'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

-- Set password for the user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';

-- grant usage for everything on the db and tables(*.*)
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- grant the user only select previlege on the 'performance_schema' db
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- grant all previleges for the hbnb_dev_db only.
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- flush changes
FLUSH PRIVILEGES;
