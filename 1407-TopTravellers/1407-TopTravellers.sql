-- Last updated: 9/11/2026, 9:34:51 AM
select name, coalesce(sum(distance),0) as travelled_distance
from users u 
left join rides r 
on u.id = r.user_id
group by name,u.id
order by travelled_distance desc, name asc;