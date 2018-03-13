USE lead_gen_business;

-- 1. What query would you run to get the total revenue for March of 2012?
SELECT SUM(amount) AS total_rev, DATE_FORMAT(charged_datetime, '%Y-%m') AS month
FROM billing
WHERE DATE_FORMAT(charged_datetime, '%Y-%m') = '2012-03' ;

-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT SUM(amount) AS total_rev, billing.client_id
FROM billing
WHERE billing.client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
SELECT domain_name, client_id
FROM sites
WHERE client_id = 10 ;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?

SELECT client_id, COUNT(site_id) AS sites_count, MONTHNAME(created_datetime) AS month , YEAR(created_datetime) AS year
FROM sites
WHERE client_id = 1 -- or 20
GROUP BY 3, 4
ORDER BY 4, 3 ;

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS leads_count, DATE_FORMAT(leads.registered_datetime , '%Y-%m-%d') AS date_generates
FROM leads
JOIN sites ON leads.site_id = sites.site_id
WHERE DATE_FORMAT(leads.registered_datetime , '%Y%m%d') BETWEEN  '20110101' AND '20110215' 
GROUP BY leads.site_id ;

-- 6. What query would you run to get a list of client names 
-- and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name,' ', clients.last_name) AS client, COUNT(leads.leads_id) AS lead_count
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE DATE_FORMAT(leads.registered_datetime , '%Y%m%d') BETWEEN  '20110101' AND '20111231' 
GROUP BY 1
ORDER BY 2 DESC ;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name,' ', clients.last_name) AS client, COUNT(leads.leads_id) AS lead_count, YEAR(leads.registered_datetime) ,MONTH(leads.registered_datetime) 
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE YEAR(leads.registered_datetime) = 2011
AND MONTH(leads.registered_datetime) BETWEEN 1 AND 6
GROUP BY 1
ORDER BY 4 DESC ;

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011?
-- Order this query by client id.

SELECT clients.client_id, CONCAT(clients.first_name,' ', clients.last_name) AS client,
COUNT(leads.leads_id) AS lead_count
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE YEAR(leads.registered_datetime) = 2011
GROUP BY 1
ORDER BY 3 DESC;

-- Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
SELECT clients.client_id, CONCAT(clients.first_name,' ', clients.last_name) AS client, sites.domain_name, 
COUNT(leads.leads_id) AS lead_count
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
GROUP BY sites.domain_name
ORDER BY  4 DESC ;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.

SELECT clients.client_id, CONCAT(clients.first_name,' ', clients.last_name) AS client, SUM(billing.amount),  MONTHNAME(billing.charged_datetime) AS month , YEAR(billing.charged_datetime) AS year
FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY client_id, month ,year 
ORDER  BY 1, 5, MONTH(billing.charged_datetime) ;


-- 10. Write a single query that retrieves all the sites that each client owns. 
-- Group the results so that each row shows a new client. 
-- It will become clearer when you add a new field called 'sites' that has all the sites that the client owns.
-- (HINT: use GROUP_CONCAT)

SELECT clients.client_id, CONCAT(clients.first_name,' ', clients.last_name) AS client,
GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') AS sites
FROM clients
JOIN sites ON sites.client_id = clients.client_id 
GROUP BY clients.client_id

