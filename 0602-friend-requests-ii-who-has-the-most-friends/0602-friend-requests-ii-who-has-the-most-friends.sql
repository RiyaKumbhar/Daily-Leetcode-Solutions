# Write your MySQL query statement below
Select id, Count(*) as num 
from (
    select requester_id as id from RequestAccepted
    Union all
    select accepter_id as id from RequestAccepted
) as all_ids
group by id
order by num desc
limit 1;