-- LeetCode: Duplicate Emails
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/duplicate-emails/

# Write your MySQL query statement below
select email from person group by(email) having count(*)>1;
