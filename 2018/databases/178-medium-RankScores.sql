# Write your MySQL query statement below
select s1.Score, (
    select count(distinct Score) Score
    from Scores s2
    where s2.Score >= s1.Score
) Rank
from Scores s1
order by Rank

# follow up: there are holes exist
# from https://leetcode.com/problems/rank-scores/discuss/202441/SQL-and-one-follow-up
select s1.Score, (
    select count(Score) + 1 Score
	from Scores s2
	where s2.Score >= s1.Score
) Rank
from Scores s1
order by rank
