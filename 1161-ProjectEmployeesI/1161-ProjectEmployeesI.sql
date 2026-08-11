-- Last updated: 8/11/2026, 6:40:01 PM
# Write your MySQL query statement below

select lt.project_id,ROUND(avg(rt.experience_years),2) as average_years
from Project as lt
left join Employee as rt
on rt.employee_id=lt.employee_id
group by lt.project_id;