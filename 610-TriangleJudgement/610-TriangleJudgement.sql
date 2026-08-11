-- Last updated: 8/11/2026, 6:42:54 PM
# Write your MySQL query statement below
# Write your MySQL query statement below
select *, (case when x+y>z and y+z>x and z+x>y then "Yes" else "No" end) as triangle  
from Triangle 