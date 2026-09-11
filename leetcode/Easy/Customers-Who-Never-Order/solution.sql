-- LeetCode: Customers Who Never Order
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/customers-who-never-order/

SELECT 
    c.name as Customers
FROM
    customers as c
LEFT JOIN
    orders as o
    ON o.customerId=c.id
WHERE
    o.id is NULL
