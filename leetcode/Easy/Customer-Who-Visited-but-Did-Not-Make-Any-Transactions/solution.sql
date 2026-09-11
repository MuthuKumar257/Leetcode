-- LeetCode: Customer Who Visited but Did Not Make Any Transactions
-- Difficulty: Easy
-- Language: MySQL
-- Problem: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

# Write your MySQL query statement below

select customer_id , count(visit_id) as count_no_trans from Visits
where 
visit_id not in (select  visit_id from Transactions)
group by customer_id;
