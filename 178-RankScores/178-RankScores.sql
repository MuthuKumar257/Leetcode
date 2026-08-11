-- Last updated: 8/11/2026, 6:47:33 PM
# Write your MySQL query statement below
select score, DENSE_RANK() over (ORDER BY score DESC) as 'rank'
from Scores
order by score DESC