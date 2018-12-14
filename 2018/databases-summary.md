
## Summary

#### 175. Combine Two Tables

- My solution

  Left join.

#### 176. Second Highest Salary

- My solution

Sub-query: query from sub-query where the 1st highest salary is returned - filter it.

- Public solution

`LIMIT` and `OFFSET`; `IFULL()`.

#### 178. Rank Scores

- My solution (**NO AC SOLUTION**)
- Public solution

Self join: the number of Scores larger than current Score relate to the rank. Use a sub-query in `SELECT` clause to do the self join.

#### 181. Employees Earning More Than Their Managers

- My solution

Self join.

#### 182. Duplicate Emails

- My solution

Group by then find the Email with count number greater than 1.

#### 183. Customers Who Never Order

- My solution

Sub-query and `NOT IN`.

#### 184. Department Highest Salary

- My solution

Simple group by and `IN` clause: get the maximum salary and Id first, then select rows that have that salary and Id. But this cannot generalize to **top n** problem.

Self join: similar to #178. Use sub-query in the `WHERE` clause.

#### 185. Department Top Three Salaries

- My solution

Similar with self join solution of #184. The only thing to change is in `COUNT()`: add `DISTINCT` in it to get the distinct top 3 salaries. In other words, the number could be larger than 3 with duplicate salaries exist.

#### 196. Delete Duplicate Emails

- My solution (**NO AC SOLUTION**)
- Public solution

Delete from self join table.

#### 197. Rising Temperature

- My solution (**NO AC SOLUTION**)
- Public solution

`SUBDATE()` and `DATEDIFF()`.

#### 595. Big Countries

- My solution

`WHERE` and `OR`.

#### 596. Classes More Than 5 Students

- My solution

Group by and `DISTINCT` in `COUNT()`.

#### 620. Not Boring Movies

- My solution

`MOD()`.

#### 627. Swap Salary

- My solution

`CASE WHEN` clause.

#### X. Tips and Notice
