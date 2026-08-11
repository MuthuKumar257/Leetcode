-- Last updated: 8/11/2026, 6:43:17 PM
select customer_number from orders  group by customer_number ORDER BY COUNT(order_number) DESC 
LIMIT 1;;