-- LeetCode: Managers with at Least 5 Direct Reports
-- Difficulty: Medium
-- Language: MySQL
-- Problem: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

# Write your MySQL query statement below
with cte as (
    select  a.name as name,a.id as idd,a.managerId as am,b.managerId as bm from employee as a
    left join employee as b
    on a.id=b.managerId
    group by b.managerId
    having  count(*)>=5
) select name  from cte  
where idd=bm
