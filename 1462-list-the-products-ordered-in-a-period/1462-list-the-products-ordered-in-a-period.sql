# Write your MySQL query statement below
select  product_name, sum(unit) as unit from Products p join Orders o on p.product_id = o.product_id where date_format(order_date,'%Y-%m') = '2020-02'
group by o.product_id
having sum(unit) >= 100