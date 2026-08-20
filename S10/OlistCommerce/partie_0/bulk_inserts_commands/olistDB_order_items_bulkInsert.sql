USE OlistCommerce;
GO

-- ============================================================================
-- 1. CRÉATION DE LA TABLE DE STAGING
-- ============================================================================
IF OBJECT_ID('dbo.order_items_staging', 'U') IS NOT NULL
    DROP TABLE dbo.order_items_staging;
GO

CREATE TABLE dbo.order_items_staging (
    order_id VARCHAR(MAX),
    order_item_id VARCHAR(MAX),
    product_id VARCHAR(MAX),
    seller_id VARCHAR(MAX),
    shipping_limit_date VARCHAR(MAX),
    price VARCHAR(MAX),
    freight_value VARCHAR(MAX)
);
GO

-- ============================================================================
-- 2. IMPORTATION DU FICHIER CSV DANS LA TABLE STAGING
-- ============================================================================
BULK INSERT dbo.order_items_staging
FROM 'D:\PROJECTS\AKIENI\DOCUMENTS\RESOURCES\archive\olist_order_items_dataset.csv'
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
INSERT INTO dbo.order_items (
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
)
SELECT 
    TRIM(order_id),
    TRY_CAST(TRIM(order_item_id) AS INT),
    TRIM(product_id),
    TRIM(seller_id),
    TRY_CAST(TRIM(shipping_limit_date) AS DATETIME),
    TRY_CAST(REPLACE(TRIM(price), ',', '.') AS DECIMAL(10,2)),
    TRY_CAST(REPLACE(TRIM(freight_value), ',', '.') AS DECIMAL(10,2))
FROM dbo.order_items_staging
WHERE NULLIF(TRIM(order_id), '') IS NOT NULL 
  AND NULLIF(TRIM(order_item_id), '') IS NOT NULL;
GO

-- ============================================================================
-- 4. NETTOYAGE DE LA TABLE TEMPORAIRE
-- ============================================================================
DROP TABLE dbo.order_items_staging;
GO