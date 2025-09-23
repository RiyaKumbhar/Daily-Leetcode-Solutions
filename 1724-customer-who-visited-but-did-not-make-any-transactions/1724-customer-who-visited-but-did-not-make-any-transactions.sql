# Write your MySQL query statement below
Select customer_id, COUNT(*) as count_no_trans
from Visits v LEFT JOIN Transactions t on v.visit_id = t.visit_id
where transaction_id is NULL 
GROUP BY customer_id
