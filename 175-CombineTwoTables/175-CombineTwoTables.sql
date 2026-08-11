-- Last updated: 8/11/2026, 6:47:42 PM
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;