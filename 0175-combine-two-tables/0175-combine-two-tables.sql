SELECT
  
   Person.lastName,
   person.firstName,
   Address.city,
   Address.state
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId;
