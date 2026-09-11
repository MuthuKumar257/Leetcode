-- Last updated: 9/11/2026, 9:34:57 AM
# Write your MySQL query statement below
SELECT stock_name,  SUM(IF(operation='buy',-price,price)) as capital_gain_loss
from  Stocks
group by stock_name