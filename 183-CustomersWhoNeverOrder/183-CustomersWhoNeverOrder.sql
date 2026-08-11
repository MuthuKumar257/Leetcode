-- Last updated: 8/11/2026, 6:47:18 PM
SELECT 
    c.name as Customers
FROM
    customers as c
LEFT JOIN
    orders as o
    ON o.customerId=c.id
WHERE
    o.id is NULL