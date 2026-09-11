-- LeetCode: Product Sales Analysis I
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/product-sales-analysis-i/

# Write your MySQL query statement below
# Write your MySQL query statement below
select p.product_name , s.year , s.price
from Sales as s
Left Join Product as p
ON s.product_id = p.product_id
