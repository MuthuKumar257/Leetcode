-- Last updated: 8/11/2026, 6:37:17 PM
# Write your MySQL query statement below

SELECT u.name, SUM(t.amount) AS balance
FROM users u
LEFT JOIN transactions t
    ON u.account=t.account
GROUP BY u.name
HAVING SUM(t.amount)>10000