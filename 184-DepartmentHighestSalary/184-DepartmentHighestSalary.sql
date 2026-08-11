-- Last updated: 8/11/2026, 6:47:15 PM
select d.name as department, e.name as employee, e.salary
from employee e,department d, (
    select departmentid, max(salary) as salary
    from employee
    group by departmentid
)m
where d.id=e.departmentid
and e.salary=m.salary
and m.departmentid=d.id;