-- Last updated: 9/11/2026, 9:32:57 AM
SELECT 
    user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)),
        LOWER(SUBSTRING(name, 2, LENGTH(name)))
    ) AS name
FROM users  
ORDER BY user_id ASC;