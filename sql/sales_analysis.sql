-- 1. Total penjualan RetailMart
SELECT
    ROUND(SUM(sales)::numeric, 2) AS total_sales
FROM sales_transactions;

-- 2. Kategori produk yang menghasilkan penjualan tertinggi
SELECT
    category,
    ROUND(SUM(sales)::numeric, 2) AS total_sales
FROM sales_transactions
GROUP BY category
ORDER BY total_sales DESC;

-- 3. Produk yang paling banyak terjual
SELECT
    product_name,
    SUM(quantity) AS total_quantity_sold
FROM sales_transactions
GROUP BY product_name
ORDER BY total_quantity_sold DESC
LIMIT 10;

-- 4. Wilayah yang menghasilkan penjualan tertinggi
SELECT
    region,
    ROUND(SUM(sales)::numeric, 2) AS total_sales
FROM sales_transactions
GROUP BY region
ORDER BY total_sales DESC;

-- 5. Perkembangan penjualan setiap bulan
SELECT
    TO_CHAR(order_date, 'YYYY-MM') AS sales_month,
    ROUND(SUM(sales)::numeric, 2) AS total_sales
FROM sales_transactions
GROUP BY TO_CHAR(order_date, 'YYYY-MM')
ORDER BY sales_month;

