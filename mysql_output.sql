select * from music_store_data.employee;
select * from music_store_data.invoice;
select * from music_store_data.genre; 
select * from music_store_data.invoice_line;
select * from music_store_data.customer;
select * from music_store_data.album2;
select * from music_store_data.artist;
select * from music_store_data.track;
//Question Set 1 - Easy

//1.Who is the senior most employee based on job title?

SELECT first_name, last_name, title 
FROM music_store_data.employee 
ORDER BY levels DESC 
LIMIT 1;

//2.Which countries have the most Invoices?

SELECT billing_country, COUNT(*) AS total_invoices
FROM music_store_data.invoice
GROUP BY billing_country
ORDER BY total_invoices DESC;

//3.What are top 3 values of total invoice?

SELECT total
FROM music_store_data.invoice
ORDER BY total DESC
LIMIT 3;

//4.Which city has the best customers? (Highest total invoice amount)

SELECT billing_city, SUM(total) AS total_sales
FROM music_store_data.invoice
GROUP BY billing_city
ORDER BY total_sales DESC
LIMIT 1;

//5.Who is the best customer? (Most money spent)

SELECT c.customer_id, c.first_name, c.last_name, SUM(i.total) AS total_spent
FROM  music_store_data.customer c
JOIN music_store_data.invoice i ON c.customer_id = i.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC
LIMIT 1;

//Question Set 2 - Moderate

//1.Write query to return the email, first name, last name, & Genre of all Rock Music listeners. Return your list ordered alphabetically by email starting with A.

SELECT DISTINCT c.email, c.first_name, c.last_name, g.name AS genre_name
FROM music_store_data.customer c
JOIN music_store_data.invoice i ON c.customer_id = i.customer_id
JOIN music_store_data.invoice_line il ON i.invoice_id = il.invoice_id
JOIN music_store_data.track t ON il.track_id = t.track_id
JOIN music_store_data.genre g ON t.genre_id = g.genre_id
WHERE g.name = 'Rock'
ORDER BY c.email ASC;

//2.Lets invite the artists who have written the most rock music in our dataset. Write a query that returns the Artist name and total track count of the top 10 rock bands. 

SELECT ar.name AS artist_name, COUNT(t.track_id) AS total_rock_tracks
FROM music_store_data.artist ar
JOIN music_store_data.album al ON ar.artist_id = al.artist_id
JOIN music_store_data.track t ON al.album_id = t.album_id
JOIN music_store_data.genre g ON t.genre_id = g.genre_id
WHERE g.name = 'Rock'
GROUP BY ar.artist_id, ar.name
ORDER BY total_rock_tracks DESC
LIMIT 10;

//3.Return all the track names that have a song length longer than the average song length. Return the Name and Milliseconds for each track. Order by the song length with the longest songs listed first.

SELECT name, milliseconds
FROM music_store_data.track
WHERE milliseconds > (SELECT AVG(milliseconds) FROM Track)
ORDER BY milliseconds DESC;

//Question Set 3 - Advance

//1.Find how much amount spent by each customer on artists? Write a query to return customer name, artist name and total spent. 

SELECT c.first_name, c.last_name, ar.name AS artist_name, SUM(il.unit_price * il.quantity) AS total_spent
FROM music_store_data.customer c
JOIN music_store_data.invoice i ON c.customer_id = i.customer_id
JOIN music_store_data.invoice_line il ON i.invoice_id = il.invoice_id
JOIN music_store_data.track t ON il.track_id = t.track_id
JOIN music_store_data.album2 al ON t.album_id = al.album_id
JOIN music_store_data.artist ar ON al.artist_id = ar.artist_id
GROUP BY c.customer_id, c.first_name, c.last_name, ar.artist_id, ar.name
ORDER BY c.first_name, c.last_name, total_spent DESC;

//2.We want to find out the most popular music Genre for each country. We determine the most popular genre as the genre with the highest amount of purchases. Write a query that returns each country along with the top Genre. For countries where the maximum number of purchases is shared return all Genres

WITH CustomerCountrySpending AS (
    SELECT 
        c.customer_id, c.first_name, c.last_name, i.billing_country, SUM(i.total) AS total_spent,
        RANK() OVER (PARTITION BY i.billing_country ORDER BY SUM(i.total) DESC) AS rank_num
    FROM music_store_data.customer c
    JOIN music_store_data.invoice i ON c.customer_id = i.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name, i.billing_country
)
SELECT billing_country, first_name, last_name, total_spent
FROM CustomerCountrySpending
WHERE rank_num = 1
ORDER BY billing_country, total_spent DESC;

//3.Write a query that determines the customer that has spent the most on music for each country. Write a query that returns the country along with the top customer and how much they spent. For countries where the top amount spent is shared, provide all customers who spent this amount

WITH CustomerCountrySpending AS (
    SELECT
        c.customer_id, c.first_name, c.last_name, i.billing_country, SUM(i.total) AS total_spent,
        RANK() OVER (PARTITION BY i.billing_country ORDER BY SUM(i.total) DESC) AS rank_num
    FROM Customer c
    JOIN Invoice i ON c.customer_id = i.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name, i.billing_country
)
SELECT billing_country, first_name, last_name, total_spent
FROM CustomerCountrySpending
WHERE rank_num = 1
ORDER BY billing_country, total_spent DESC;