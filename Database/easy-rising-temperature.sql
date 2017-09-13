-- https://leetcode.com/problems/rising-temperature/description/
select w2.Id  
from Weather w1 left join Weather as w2 on datediff(w2.Date, w1.Date) = 1
where w1.Temperature < w2.Temperature