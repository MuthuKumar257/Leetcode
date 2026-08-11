-- Last updated: 8/11/2026, 6:42:41 PM
# Write your MySQL query statement below
SELECT ROW_NUMBER() OVER() id, student
FROM seat
ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)