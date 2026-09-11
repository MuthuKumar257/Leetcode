-- LeetCode: Second Highest Salary
-- Difficulty: Medium
-- Language: MySQL
-- Problem: https://leetcode.com/problems/second-highest-salary/

# Write your MySQL query statement below
select
(select distinct Salary 
from Employee order by salary desc 
limit 1 offset 1) 
as SecondHighestSalary;
