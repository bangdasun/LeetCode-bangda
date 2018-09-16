-- https://leetcode.com/problems/customers-who-never-order/description/
select Name as Customers
from Customers as c
where c.Id not in (select o.CustomerId from Orders as o)