-- Last updated: 8/11/2026, 6:39:50 PM
# Write your MySQL query statement below
# Write your MySQL query statement below

SELECT ROUND(SUM(login)/COUNT(DISTINCT player_id), 2) AS fraction
FROM (
  SELECT
    player_id,
    DATEDIFF(event_date, MIN(event_date) OVER(PARTITION BY player_id)) = 1 AS login
  FROM Activity
) AS t