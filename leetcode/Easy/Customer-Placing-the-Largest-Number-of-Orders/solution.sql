-- LeetCode: Customer Placing the Largest Number of Orders
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

select customer_number from orders  group by customer_number ORDER BY COUNT(order_number) DESC 
LIMIT 1;;
