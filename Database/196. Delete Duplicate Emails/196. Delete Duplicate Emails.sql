# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below


delete from Person p1
where p1.id NOT IN (select min(id) from Person p2 group by p2.email)