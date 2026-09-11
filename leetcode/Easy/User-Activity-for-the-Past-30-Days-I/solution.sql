-- LeetCode: User Activity for the Past 30 Days I
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

# Write your MySQL query statement below

SELECT 
    a.activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM activity a
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date;
