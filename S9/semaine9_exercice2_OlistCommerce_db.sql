
-- Exercice 1
CREATE DATABASE OlistCommerce;
GO

USE OlistCommerce;
GO

-- Exercice 2
CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50) NOT NULL,
    customer_zip_code_prefix VARCHAR(10) NOT NULL,
    customer_city VARCHAR(100),
    customer_state CHAR(2)
);
GO

CREATE TABLE sellers (
    seller_id VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix VARCHAR(10) NOT NULL,
    seller_city VARCHAR(100),
    seller_state CHAR(2)
);
GO

CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name VARCHAR(100),
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm DECIMAL(8,2),
    product_height_cm DECIMAL(8,2),
    product_width_cm DECIMAL(8,2)
);
GO

CREATE TABLE product_category_name_translation (
    product_category_name VARCHAR(100) PRIMARY KEY,
    product_category_name_english VARCHAR(100)
);
GO

-- Exercice 3
CREATE TABLE orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    order_status VARCHAR(30) NOT NULL,
    order_purchase_timestamp DATETIME NOT NULL,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME NOT NULL,
    CONSTRAINT FK_orders_customers FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
GO

CREATE TABLE order_items (
    order_id VARCHAR(50) NOT NULL,
    order_item_id INT NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    seller_id VARCHAR(50) NOT NULL,
    shipping_limit_date DATETIME,
    price DECIMAL(10,2) NOT NULL,
    freight_value DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_order_items PRIMARY KEY (order_id, order_item_id),
    CONSTRAINT FK_order_items_orders FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT FK_order_items_products FOREIGN KEY (product_id) REFERENCES products(product_id),
    CONSTRAINT FK_order_items_sellers FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);
GO

CREATE TABLE order_payments (
    order_id VARCHAR(50) NOT NULL,
    payment_sequential INT NOT NULL,
    payment_type VARCHAR(30) NOT NULL,
    payment_installments INT,
    payment_value DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_order_payments PRIMARY KEY (order_id, payment_sequential),
    CONSTRAINT FK_order_payments_orders FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
GO

CREATE TABLE order_reviews (
    review_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50) NOT NULL,
    review_score INT NOT NULL,
    review_comment_title VARCHAR(200),
    review_comment_message NVARCHAR(MAX),
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME,
    CONSTRAINT FK_order_reviews_orders FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
GO

-- Exercice 4
ALTER TABLE order_reviews
ADD CONSTRAINT CHK_review_score CHECK (review_score BETWEEN 1 AND 5);
GO

-- Exercice 5
ALTER TABLE order_items
ADD total_value AS (price + freight_value);
GO

-- Exercice 6
ALTER TABLE products
ADD product_brand VARCHAR(100),
    is_active BIT NOT NULL DEFAULT 1;
GO

-- Exercice 7
CREATE TABLE test_import (
    id INT,
    nom VARCHAR(50),
    valeur DECIMAL(10,2)
);
GO

EXEC sp_rename 'test_import', 'test_import_v2';
GO

ALTER TABLE test_import_v2
ADD commentaire VARCHAR(100);
GO

DROP TABLE test_import_v2;
GO

-- Exercice 8
CREATE TABLE order_audit (
    audit_id INT IDENTITY(1,1) PRIMARY KEY,
    order_id VARCHAR(50),
    action_type VARCHAR(20),
    action_date DATETIME DEFAULT GETDATE(),
    performed_by VARCHAR(50) DEFAULT SYSTEM_USER
);
GO

-- Exercice 9
CREATE NONCLUSTERED INDEX IX_orders_status_purchasedate
ON orders (order_status, order_purchase_timestamp);
GO

-- Exercice 10
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_CATALOG = 'OlistCommerce'
ORDER BY TABLE_NAME, ORDINAL_POSITION;
GO