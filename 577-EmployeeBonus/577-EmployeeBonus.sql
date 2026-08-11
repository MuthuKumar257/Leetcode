-- Last updated: 8/11/2026, 6:43:24 PM
# Write your MySQL query statement below
select name,bonus from employee e  left outer join  bonus b on b.empid=e.empid   where b.bonus<1000 or bonus is null;