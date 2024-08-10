-- 3. Database Testing with SQL:
-- Given a database table 'users' with columns 'userID', 'username', 'password', 'Email', and 'CreateDate', 
-- write SQL queries to:
--  - Retrieve all users who regestered in the last 30 days
--   - Find the total number of users with a specific domain in their email (e.g. all users with emails ending in 
--   '@example.com')
--   -Update the email of a user with specific  'UserId'.

-- Retrieve all users who registered in the last 30 days:
SELECT *
FROM users
WHERE CreateDate >= CURDATE() - INTERVAL 30 DAY;

-- Find the total number of users with a specific domain in their email:
SELECT COUNT(*)
FROM users
WHERE Email LIKE '%@example.com';

-- Update the email of a user with a specific UserID:
UPDATE users
SET Email = 'newemail@example.com'
WHERE userID = 12345;



