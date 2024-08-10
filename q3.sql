-- 3. Database Testing with SQL:
-- Given a database table 'users' with columns 'userID', 'username', 'password', 'Email', and 'CreateDate', 
-- write SQL queries to:
--  - Retrieve all users who regestered in the last 30 days
--   - Find the total number of users with a specific domain in their email (e.g. all users with emails ending in 
--   '@example.com')
--   -Update the email of a user with specific  'UserId'. get current date in sql Programiz

-- Retrieve all users who registered in the last 30 days: 

CREATE TABLE users (
    userID INT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255),
    Email VARCHAR(100),
    CreateDate DATE
);

INSERT INTO users (userID, username, password, Email, CreateDate) VALUES
(1, 'john_doe', 'password123', 'john.doe@example.com', '2024-07-12'),
(2, 'jane_smith', 'password456', 'jane.smith@example.com', '2024-07-30'),
(3, 'alice_jones', 'password789', 'alice.jones@example.com', '2024-05-30'),
(4, 'bob_brown', 'password000', 'bob.brown@example.com', '2024-07-05'),
(5, 'carol_white', 'password111', 'carol.white@example.com', '2024-04-10'),
(6, 'dave_black', 'password222', 'dave.black@example.com', '2023-06-15');
 



SELECT *
FROM users
WHERE CreateDate >= date('now', '-30 days');


-- Find the total number of users with a specific domain in their email:
SELECT COUNT(*)
FROM users
WHERE Email LIKE '%@example.com';

-- Update the email of a user with a specific UserID:
UPDATE users
SET Email = 'newemail@example.com'
WHERE userID = 1;

UPDATE users
SET Email = 'newemail@example.com'
WHERE userID = 2;



