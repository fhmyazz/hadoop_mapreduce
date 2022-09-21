-- Example DWH

DROP TABLE IF EXISTS dim_orders;
CREATE TABLE dim_orders (
	order_id INT NOT NULL,
	order_date DATE NOT NULL,
	user_id INT NOT NULL,
	payment_name VARCHAR(255),
	shipper_name VARCHAR(255),
	order_price INT,
	order_discount INT,
	voucher_name VARCHAR(255),
	voucher_price INT,
	order_total INT,
	rating_status VARCHAR(255)
	);

-- DROP TABLE IF EXISTS fact_order_items; 
-- CREATE TABLE fact_order_items (
-- 	order_item_id INT NOT NULL ,
-- 	order_id INT NOT NULL,
-- 	product_id INT NOT NULL,
-- 	order_item_quantity INT,
-- 	product_discount INT,
-- 	product_subdiscount INT,
-- 	product_price INT NOT NULL,
-- 	product_subprice INT NOT NULL
-- );