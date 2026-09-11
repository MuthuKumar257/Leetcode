-- LeetCode: Replace Employee ID With The Unique Identifier
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT
EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id
