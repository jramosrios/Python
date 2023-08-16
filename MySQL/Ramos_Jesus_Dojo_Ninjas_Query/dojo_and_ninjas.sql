SELECT * FROM dojo_and_ninjas_schema.dojos;
SELECT * FROM dojo_and_ninjas_schema.ninjas;

INSERT INTO dojos (fname, created_at, updated_at)
VALUES ("James", NOW(), NOW());

SET SQL_SAFE_UPDATES = 0;
DELETE fROM dojos;

INSERT INTO dojos (fname, created_at, updated_at)
VALUES ("Colorado", NOW(), NOW());
INSERT INTO dojos (fname, created_at, updated_at)
VALUES ("Florida", NOW(), NOW());
INSERT INTO dojos (fname, created_at, updated_at)
VALUES ("Arizona", NOW(), NOW());

INSERT INTO ninjas (first_name, last_name, age,created_at, updated_at, dojo_id)
VALUES ("Nicole", "Medina", 23, NOW(), NOW(), 10), ("Ruben", "Rivera", 21, NOW(), NOW(), 10),("Anapaula", "Sanchez", 21, NOW(), NOW(), 10);
INSERT INTO ninjas (first_name, last_name, age,created_at, updated_at, dojo_id)
VALUES ("Jesus", "Ramos", 25, NOW(), NOW(), 11), ("Jose", "Ramos", 29, NOW(), NOW(), 11),("Reina", "Rosario", 22, NOW(), NOW(), 11);

INSERT INTO ninjas (first_name, last_name, age,created_at, updated_at, dojo_id)
VALUES ("Maria", "Rios", 62, NOW(), NOW(), 12), ("Jose", "Rivera", 41, NOW(), NOW(), 12),("Juan", "Rovira", 21, NOW(), NOW(), 12);

SELECT * FROM ninjas
WHERE dojo_id =10;

SELECT * FROM ninjas
WHERE dojo_id =12;