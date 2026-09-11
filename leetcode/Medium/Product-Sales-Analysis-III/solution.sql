-- LeetCode: Product Sales Analysis III
-- Difficulty: Medium
-- Language: MySQL
-- Problem: https://leetcode.com/problems/product-sales-analysis-iii/

WITH first_year_sales AS (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

SELECT
    s.product_id,
    fy.first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN first_year_sales fy
    ON s.product_id = fy.product_id
WHERE s.year = fy.first_year;
