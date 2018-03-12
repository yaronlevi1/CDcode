
SELECT * FROM users ;

SELECT first_name, last_name from users;

SELECT first_name as first, last_name as last from users;

SELECT * from users
where id=1 or id =2
order by birthday desc ;


SELECT * 
FROM users
WHERE first_name LIKE "%e";

SELECT * 
FROM users
WHERE first_name LIKE "K%";

SELECT *
FROM users
WHERE first_name LIKE "%e"
ORDER BY birthday DESC;

SELECT first_name
FROM users
ORDER BY first_name ;

SELECT * FROM tweets ;

INSERT INTO `twitter`.`tweets` 
(`tweet`, `user_id`, `created_at`, `updated_at`) 
 VALUES ('where does dust come from?', '1', NOW(), NOW() );

SELECT * FROM users ;

UPDATE `twitter`.`users`
SET `first_name`='Jerome' 
WHERE `id`='6';

DELETE FROM `twitter`.`users`
WHERE `id`='6';

# WHERE name = 'France'
# WHERE name IN ('Brazil', 'Russia', 'India', 'China');
# WHERE area BETWEEN 250000 AND 300000

SELECT * FROM users ;



SELECT CONCAT('mr. ' , first_name, " ", last_name) AS full_name,  handle AS nickname FROM users;

SELECT CONCAT_WS('***', first_name, last_name, "cool") AS full_name,  handle AS nickname FROM users;

SELECT LENGTH(last_name) AS len_last_name FROM users;

SELECT LOWER(last_name) AS lower, last_name FROM users;

SELECT HOUR(birthday), DAYNAME(birthday), MONTH(birthday) , NOW() FROM users;

SELECT HOUR(birthday), DAYNAME(birthday), MONTH(birthday) , NOW() FROM users;

SELECT DATE_FORMAT(NOW(), '%W %M %m  %e, %Y') As weird_time_format;

/*
REPLACE()
SUBSTRING()

ABS()
MOD()
RAND()
ROUND()

TIME_FORMAT()
*/

USE lead_gen_business ;

SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
from clients
JOIN billing ON clients.id = billing.clients_id ;

SELECT clients.first_name AS client_first_name , clients.last_name, sites.domain_name, leads.first_name AS lead_first_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id ;

SELECT clients.first_name  , clients.last_name, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.id = sites.clients_id ;

SELECT clients.first_name, clients.last_name, SUM(billing.amount)
from clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id ;


SELECT GROUP_CONCAT(' || ',sites.domain_name), clients.first_name, clients.last_name
FROM clients
JOIN sites ON clients.id = sites. clients_id
GROUP BY clients_id ;

SELECT COUNT(leads.id), sites.domain_name
FROM sites
JOIN leads on sites.id = leads.sites_id
GROUP BY sites.id ;









/*
MIN()
MAX()
AVG()
*/


SELECT clients.company, SUM(billing.amount) AS total_sales 
FROM clients 
LEFT JOIN billing 
ON billing.client_id = client.id 
GROUP BY clients.company HAVING SUM(billing.amount) > 3500;


SELECT id, first_name FROM users LIMIT 11,10 



























	
