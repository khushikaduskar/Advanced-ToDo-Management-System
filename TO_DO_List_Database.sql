-- Create Database
CREATE DATABASE IF NOT EXISTS todo_db;

-- Use Database
USE todo_db;

-- Create Tasks Table
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    priority ENUM('High', 'Medium', 'Low') DEFAULT 'Medium',
    due_date DATE,
    status ENUM('Pending', 'Completed') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verify Table Structure
DESCRIBE tasks;

-- View All Tasks
SELECT * FROM tasks; giveme updated in this code onlt for id