-- Last updated: 9/11/2026, 9:35:02 AM
# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT
EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id