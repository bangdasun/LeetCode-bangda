# Write your MySQL query statement below
select w1.Id
from Weather w1 left join Weather w2 on w2.RecordDate = subdate(w1.RecordDate, 1)
where w1.Temperature > w2.Temperature

# Write your MySQL query statement below
select w1.Id
from Weather w1 left join Weather w2 on datediff(w1.RecordDate, w2.RecordDate) = 1
where w1.Temperature > w2.Temperature