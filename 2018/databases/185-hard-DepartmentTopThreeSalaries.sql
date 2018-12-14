# Write your MySQL query statement below
# CHANGE count(*) to count(distinct e2.Salary)
# before change:
# last tie will be counted
# if 2,1,1,0:
# return 2,1,1
#
# if 2,1,0,0:
# return 2,1,0,0
select d.Name Department, tmp.Name Employee, tmp.Salary Salary
from (select *
      from Employee e1
      where (select count(*)
             from Employee e2
             where e1.DepartmentId = e2.DepartmentId
               and e1.Salary < e2.Salary) < 3) tmp, Department d
where tmp.DepartmentId = d.Id
order by d.Name, tmp.Salary desc