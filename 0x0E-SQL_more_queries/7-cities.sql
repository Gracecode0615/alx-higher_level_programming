-- create DB hbtn_0d_usa and table cities
-- column state_id has a foreign key the references to 
-- id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);
