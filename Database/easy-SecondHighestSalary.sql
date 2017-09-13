-- https://leetcode.com/problems/second-highest-salary/description/
select max(Salary) as SecondHighestSalary
from Employee 
where Salary not in (select max(Salary) from Employee)