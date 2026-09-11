-- Last updated: 9/11/2026, 9:38:58 AM
# Write your MySQL query statement below
select player_id,min(event_date) as first_login
from Activity
group by player_id