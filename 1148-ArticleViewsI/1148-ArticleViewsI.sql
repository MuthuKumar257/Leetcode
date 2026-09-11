-- Last updated: 9/11/2026, 9:38:19 AM
# Write your MySQL query statement below
# Write your MySQL query statement below

select distinct author_id as id from Views
where author_id = viewer_id 
order by id;