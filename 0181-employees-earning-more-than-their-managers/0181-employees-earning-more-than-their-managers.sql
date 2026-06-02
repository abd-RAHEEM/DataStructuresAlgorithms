/* Write your PL/SQL query statement below */
select a.name as Employee from Employee a join Employee b on a.managerId=b.id where a.salary>b.salary