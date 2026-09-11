-- LeetCode: Employees Earning More Than Their Managers
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Write your MySQL query statement below
SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary
