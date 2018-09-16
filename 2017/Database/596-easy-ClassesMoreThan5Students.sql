-- https://leetcode.com/problems/classes-more-than-5-students/description/
select class
from (
  select class, count(distinct student) as num_student
    from courses
    group by class
) temp
where num_student >= 5