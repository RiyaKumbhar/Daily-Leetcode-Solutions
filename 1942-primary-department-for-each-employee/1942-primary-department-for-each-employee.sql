# Write your MySQL query statement below
select  employee_id, department_id From Employee
where primary_flag = 'Y' or
employee_id in (Select employee_id from Employee group by employee_id having count(employee_id) = 1)