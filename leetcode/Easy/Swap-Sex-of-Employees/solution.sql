-- LeetCode: Swap Sex of Employees
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/swap-sex-of-employees/

# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE
        WHEN sex = 'm' THEN 'f'
        ELSE 'm'
    END;
