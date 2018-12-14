# Write your MySQL query statement below
select Name as Customers
from Customers
where Id not in (select C.Id
                 from Customers C right join Orders O on C.Id = O.CustomerId)
				 
# Write your MySQL query statement below
select Name as Customers
from Customers
where Id not in (select CustomerId from Orders)