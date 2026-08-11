-- Last updated: 8/11/2026, 6:42:58 PM
SELECT s.name FROM SalesPerson s 
	WHERE s.sales_id NOT IN (
		SELECT o.sales_id FROM Orders o LEFT JOIN Company c 
			ON c.com_id=o.com_id 
		WHERE c.name="RED"
	);