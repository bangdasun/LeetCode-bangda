-- https://leetcode.com/problems/delete-duplicate-emails/description/
-- NOT ACCEPTED
select min(Id) as Id, Email
from Person
group by Email