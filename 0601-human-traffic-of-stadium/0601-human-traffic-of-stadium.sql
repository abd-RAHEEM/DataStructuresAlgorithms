# Write your MySQL query statement below
select id, visit_date,people from Stadium s1 where people>= 100 and exists (select 1 from Stadium s2 ,Stadium s3 where s2.people>=100 and s3.people>=100 and (
    (s1.id=s2.id-1 and s1.id=s3.id-2)
    or
    (s1.id=s2.id+1 and s1.id=s3.id-1)
    or
    (s1.id=s2.id+2 and s1.id=s3.id+1)
) )
order by visit_date 