-- Write your PostgreSQL query statement below
SELECT
    FirstName,
    LastName,
    City,
    State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;