SELECT COUNT(*) AS total_products
FROM `apple_products`;
SELECT DISTINCT Platform
FROM `apple_products`;
SELECT
    Platform,
    COUNT(*) AS product_count
FROM `apple_products`
GROUP BY Platform;
SELECT
    Platform,
    COUNT(*) AS product_count
FROM `apple_products`
GROUP BY Platform;
SELECT
    Platform,
    AVG(Rating) AS average_rating
FROM `apple_products`
GROUP BY Platform;
SELECT *
FROM `apple_products`
WHERE Launch_Price_USD > 1000;
SELECT *
FROM `apple_products`
WHERE Platform = 'Amazon'
  AND Rating > 4.5;
  SELECT *
FROM `apple_products`
ORDER BY Rating DESC
LIMIT 10;
SELECT *
FROM `apple_products`
ORDER BY Reviews_Count DESC
LIMIT 10;
