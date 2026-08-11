-- Last updated: 8/11/2026, 6:43:08 PM
# Write your MySQL query statement below
select class from courses group by(class) having count(*)>4;