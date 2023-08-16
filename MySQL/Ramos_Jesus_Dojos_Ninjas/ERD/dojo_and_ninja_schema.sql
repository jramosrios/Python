SELECT * FROM dojo_and_ninjas_schema.dojos;
SELECT * from dojos
LEFT JOIN ninjas
ON dojos.id = ninjas.dojos_id
WHERE dojos.id = 2;