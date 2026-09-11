-- LeetCode: Last Person to Fit in the Bus
-- Difficulty: Medium
-- Language: MySQL
-- Problem: https://leetcode.com/problems/last-person-to-fit-in-the-bus/

# Write your MySQL query statement below
SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1
