# Write your MySQL query statement below
select P.firstName, P.lastName, A.city, A.state
from Person as P
LEFT JOIN Address as A
ON P.personId = A.personId