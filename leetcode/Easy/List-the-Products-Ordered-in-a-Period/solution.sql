-- LeetCode: List the Products Ordered in a Period
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/list-the-products-ordered-in-a-period/

SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p 
JOIN Orders o
ON o.product_id=p.product_id
WHERE o.order_date like '2020-02-%'
GROUP BY o.product_id
HAVING unit>=100;
