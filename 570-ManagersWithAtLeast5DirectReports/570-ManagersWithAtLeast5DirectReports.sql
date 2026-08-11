-- Last updated: 8/11/2026, 6:43:27 PM
# Write your MySQL query statement below
with cte as (
    select  a.name as name,a.id as idd,a.managerId as am,b.managerId as bm from employee as a
    left join employee as b
    on a.id=b.managerId
    group by b.managerId
    having  count(*)>=5
) select name  from cte  
where idd=bm 