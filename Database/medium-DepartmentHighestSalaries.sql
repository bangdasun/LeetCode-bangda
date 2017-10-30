-- https://leetcode.com/problems/department-highest-salary/description/

select dpt.Name as Department, emp.Name as Employee, emp.Salary as Salary
from Department dpt, Employee emp
where dpt.Id = emp.DepartmentId
  and (emp.DepartmentId, emp.Salary) in (select DepartmentId, max(Salary) as Salary
                                         from Employee
                                         group by DepartmentId)