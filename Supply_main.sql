CREATE DATABASE supply_chain;

USE supply_chain;

CREATE TABLE orders (
    type VARCHAR(30),
    days_for_shipment_scheduled INT,
    benefit_per_order DECIMAL(12,2),
    sales_per_customer DECIMAL(12,2),
    late_delivery_risk TINYINT,
    category_id INT,
    category_name VARCHAR(100),
    customer_city VARCHAR(100),
    customer_country VARCHAR(100),
    customer_fname VARCHAR(100),
    customer_segment VARCHAR(50),
    customer_state VARCHAR(100),
    department_id INT,
    department_name VARCHAR(100),
    market VARCHAR(50),
    order_city VARCHAR(100),
    order_country VARCHAR(100),
    order_date DATETIME,
    order_item_cardprod_id INT,
    order_item_discount DECIMAL(12,2),
    order_item_discount_rate DECIMAL(8,4),
    order_item_product_price DECIMAL(12,2),
    order_item_profit_ratio DECIMAL(8,4),
    order_item_quantity INT,
    sales DECIMAL(12,2),
    order_item_total DECIMAL(12,2),
    order_profit_per_order DECIMAL(12,2),
    order_region VARCHAR(100),
    order_state VARCHAR(100),
    order_status VARCHAR(50),
    product_category_id INT,
    product_name VARCHAR(255),
    product_price DECIMAL(12,2),
    product_status TINYINT,
    shipping_date DATETIME,
    shipping_mode VARCHAR(50),
    order_year INT,
    order_month INT,
    order_day INT,
    order_weekday INT,
    profit_margin_percentage DECIMAL(10,4)
);

describe orders;

select * from orders;

# Total Sales
SELECT
    ROUND(SUM(sales), 2) AS total_sales
FROM orders;

# Total Orders
SELECT
    COUNT(*) AS total_orders
FROM orders;

#  	Total Profit
SELECT
    ROUND(SUM(order_profit_per_order), 2) AS total_profit
FROM orders;

# Late Delivery 
SELECT
    COUNT(*) AS late_orders
FROM orders
WHERE late_delivery_risk = 1;

#  Late Delivery Percentage
SELECT
    ROUND(
        SUM(late_delivery_risk) * 100.0 / COUNT(*),
        2
    ) AS late_delivery_percentage
FROM orders;


# Sales by Market
SELECT
    market,
    COUNT(*) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(order_profit_per_order), 2) AS total_profit
FROM orders
GROUP BY market
ORDER BY total_sales DESC;


# Year-wise Sales
SELECT
    order_year,
    COUNT(*) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(order_profit_per_order), 2) AS total_profit
FROM orders
GROUP BY order_year
ORDER BY order_year;


# Top 10 Most Profitable Products
SELECT
    product_name,
    COUNT(*) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(order_profit_per_order), 2) AS total_profit
FROM orders
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;