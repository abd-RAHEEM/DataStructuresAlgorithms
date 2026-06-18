# Write your MySQL query statement below

select distinct(num) as ConsecutiveNums from (
select num, lead(num,1) over (order by id) as next_num, lead(num,2) over (order by id) as next_next_num from Logs)
as temp where num=next_num and num=next_next_num