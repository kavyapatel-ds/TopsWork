CREATE DATABASE foodie_app3;
USE foodie_app3;

CREATE TABLE restaurants3(
    id INT PRIMARY KEY,
	R_name VARCHAR(100),
    cuisine VARCHAR(50),
    rating DECIMAL(2,1),
    location VARCHAR(100)
);

CREATE TABLE users3(
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE,
    created_at DATETIME
);