# Write your MySQL query statement below
select name as Customers from Customers left join Orders on Customers.Id = Orders.Customerid where CustomerId  is Null;