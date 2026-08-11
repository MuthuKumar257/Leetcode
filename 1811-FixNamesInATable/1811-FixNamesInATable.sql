-- Last updated: 8/11/2026, 6:37:07 PM
SELECT 
    user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)),
        LOWER(SUBSTRING(name, 2, LENGTH(name)))
    ) AS name
FROM users  
ORDER BY user_id ASC;