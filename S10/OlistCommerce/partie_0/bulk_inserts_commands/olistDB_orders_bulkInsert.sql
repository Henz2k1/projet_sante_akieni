USE OlistCommerce;
GO

-- ============================================================================
-- 1. CRÉATION DE LA TABLE DE STAGING
-- ============================================================================
IF OBJECT_ID('dbo.orders_staging', 'U') IS NOT NULL
    DROP TABLE dbo.orders_staging;
GO

CREATE TABLE dbo.orders_staging (
    order_id VARCHAR(MAX),
    customer_id VARCHAR(MAX),
    order_status VARCHAR(MAX),
    order_purchase_timestamp VARCHAR(MAX),
    order_approved_at VARCHAR(MAX),
    order_delivered_carrier_date VARCHAR(MAX),
    order_delivered_customer_date VARCHAR(MAX),
    order_estimated_delivery_date VARCHAR(MAX)
);
GO

-- ============================================================================
-- 2. IMPORTATION DU FICHIER CSV DANS LA TABLE STAGING
-- ============================================================================
BULK INSERT dbo.orders_staging
FROM 'D:\PROJECTS\AKIENI\DOCUMENTS\RESOURCES\archive\olist_orders_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);
GO

-- ============================================================================
-- 3. CONVERSION ET INSERTION PROPRE DANS LA TABLE FINALE
-- ============================================================================
INSERT INTO dbo.orders (
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
)
SELECT 
    TRIM(order_id),
    TRIM(customer_id),
    TRIM(order_status),
    TRY_CAST(TRIM(order_purchase_timestamp) AS DATETIME),
    TRY_CAST(TRIM(order_approved_at) AS DATETIME),
    TRY_CAST(TRIM(order_delivered_carrier_date) AS DATETIME),
    TRY_CAST(TRIM(order_delivered_customer_date) AS DATETIME),
    TRY_CAST(TRIM(order_estimated_delivery_date) AS DATETIME)
FROM dbo.orders_staging
WHERE NULLIF(TRIM(order_id), '') IS NOT NULL;
GO

-- ============================================================================
-- 4. NETTOYAGE DE LA TABLE TEMPORAIRE
-- ============================================================================
DROP TABLE dbo.orders_staging;
GO