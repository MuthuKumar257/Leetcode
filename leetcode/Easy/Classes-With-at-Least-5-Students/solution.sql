-- LeetCode: Classes With at Least 5 Students
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/classes-with-at-least-5-students/

# Write your MySQL query statement below
select class from courses group by(class) having count(*)>4;
