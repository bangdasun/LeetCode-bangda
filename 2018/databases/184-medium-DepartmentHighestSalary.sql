# Write your MySQL query statement below
select d.Name Department, tmp.Name Employee, tmp.Salary Salary
from (
    select *
    from Employee e1
    where (select count(*)
           from Employee e2
           where e1.DepartmentId = e2.DepartmentId
             and e1.Salary < e2.Salary) < 1) tmp inner join Department d on tmp.DepartmentId = d.Id
order by tmp.Name

# Write your MySQL query statement below
select dpt.Name as Department, emp.Name as Employee, emp.Salary as Salary
from Department dpt, Employee emp
where dpt.Id = emp.DepartmentId
  and (emp.DepartmentId, emp.Salary) in (select DepartmentId, max(Salary) as Salary
                                         from Employee
                                         group by DepartmentId)