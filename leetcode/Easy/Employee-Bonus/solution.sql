-- LeetCode: Employee Bonus
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/employee-bonus/

# Write your MySQL query statement below
select name,bonus from employee e  left outer join  bonus b on b.empid=e.empid   where b.bonus<1000 or bonus is null;
