-- Last updated: 8/11/2026, 6:42:38 PM
# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE
        WHEN sex = 'm' THEN 'f'
        ELSE 'm'
    END;
 
