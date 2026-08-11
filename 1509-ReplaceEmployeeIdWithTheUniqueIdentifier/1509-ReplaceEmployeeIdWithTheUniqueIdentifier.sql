-- Last updated: 8/11/2026, 6:38:01 PM
# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT
EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id