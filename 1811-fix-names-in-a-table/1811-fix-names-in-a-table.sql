# Write your MySQL query statement below
select Users.user_id,
concat(upper(substr(Users.name,1,1)), lower(substr(Users.name,2))) as name
from users
order by Users.user_id ASC;