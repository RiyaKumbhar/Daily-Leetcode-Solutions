# Write your MySQL query statement below
select 'Low Salary' As category,
    count(if(income<20000,1,null)) as accounts_count
from Accounts

union all

select 'Average Salary',
    Count(if(income>=20000 and income<=50000,1,null))
From Accounts

union all

select 'High Salary',
    count(if(income>50000,1,null))
From Accounts;