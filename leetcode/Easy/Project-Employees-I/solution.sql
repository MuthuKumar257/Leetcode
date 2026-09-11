-- LeetCode: Project Employees I
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/project-employees-i/

# Write your MySQL query statement below

select lt.project_id,ROUND(avg(rt.experience_years),2) as average_years
from Project as lt
left join Employee as rt
on rt.employee_id=lt.employee_id
group by lt.project_id;
