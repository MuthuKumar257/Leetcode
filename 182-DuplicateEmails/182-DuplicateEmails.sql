-- Last updated: 8/11/2026, 6:47:23 PM
# Write your MySQL query statement below
select email from person group by(email) having count(*)>1;