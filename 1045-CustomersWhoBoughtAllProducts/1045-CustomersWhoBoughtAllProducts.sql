-- Last updated: 9/11/2026, 9:39:22 AM
# Write your MySQL query statement below
/* Write your PL/SQL query statement below */
SELECT customer_id FROM Customer GROUP BY customer_id HAVING 

COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)