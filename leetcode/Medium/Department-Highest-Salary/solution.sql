-- LeetCode: Department Highest Salary
-- Difficulty: Medium
-- Language: MySQL
-- Problem: https://leetcode.com/problems/department-highest-salary/

select d.name as department, e.name as employee, e.salary
from employee e,department d, (
    select departmentid, max(salary) as salary
    from employee
    group by departmentid
)m
where d.id=e.departmentid
and e.salary=m.salary
and m.departmentid=d.id;
