-- LeetCode: Product Price at a Given Date
-- Difficulty: Medium
-- Language: MySQL
-- Problem: https://leetcode.com/problems/product-price-at-a-given-date/

# Write your MySQL query statement below
SELECT product_id, new_price AS price 
FROM Products
WHERE(product_id,change_date) IN
(
    SELECT product_id, MAX(change_date)
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
UNION
SELECT product_id, 10 AS price 
FROM Products
WHERE(product_id) NOT IN
(
    SELECT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
);
