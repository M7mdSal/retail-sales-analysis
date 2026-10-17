-- Import data/sales_sample.csv into MySQL table sales (e.g. using MySQL Workbench Import Wizard).
CREATE DATABASE IF NOT EXISTS retail_sales;
USE retail_sales;
CREATE TABLE IF NOT EXISTS sales (
  order_id VARCHAR(20) PRIMARY KEY,
  date DATE NOT NULL,
  product VARCHAR(100) NOT NULL,
  category VARCHAR(50) NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10,2) NOT NULL,
  unit_cost DECIMAL(10,2) NOT NULL,
  discount DECIMAL(4,2) NOT NULL,
  city VARCHAR(50) NOT NULL
);
-- Total revenue and profit (discount is a fraction, e.g. 0.10 = 10%).
SELECT ROUND(SUM(quantity * unit_price * (1-discount)),2) AS revenue,
       ROUND(SUM(quantity * (unit_price * (1-discount) - unit_cost)),2) AS profit
FROM sales;
-- Revenue per month.
SELECT DATE_FORMAT(date, '%Y-%m') AS month,
       ROUND(SUM(quantity * unit_price * (1-discount)),2) AS revenue
FROM sales GROUP BY DATE_FORMAT(date, '%Y-%m') ORDER BY month;
-- Top five products by units sold.
SELECT product, SUM(quantity) AS units_sold
FROM sales GROUP BY product ORDER BY units_sold DESC LIMIT 5;
-- Category and city breakdown.
SELECT category, city, ROUND(SUM(quantity * unit_price * (1-discount)),2) AS revenue
FROM sales GROUP BY category, city ORDER BY revenue DESC;
