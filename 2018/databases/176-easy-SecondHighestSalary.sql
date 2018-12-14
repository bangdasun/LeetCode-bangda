# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary
from Employee
where Salary not in (
    select max(Salary)
    from Employee)

# default offset = 0, skip 0 rows
select (
    select distinct salary
    from Employee
    order by salary desc
    limit 1 offset 1) as SecondHighestSalary