-- LeetCode: Fix Names in a Table
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/fix-names-in-a-table/

SELECT 
    user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)),
        LOWER(SUBSTRING(name, 2, LENGTH(name)))
    ) AS name
FROM users  
ORDER BY user_id ASC;
