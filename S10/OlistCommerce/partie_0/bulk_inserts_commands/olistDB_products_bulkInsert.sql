USE OlistCommerce;
GO

-- ============================================================================
-- 1. CRÉATION DE LA TABLE DE STAGING
-- ============================================================================
IF OBJECT_ID('dbo.products_staging', 'U') IS NOT NULL
    DROP TABLE dbo.products_staging;
GO

CREATE TABLE dbo.products_staging (
    product_id VARCHAR(MAX),
    product_category_name VARCHAR(MAX),
    product_name_lenght VARCHAR(MAX),
    product_description_lenght VARCHAR(MAX),
    product_photos_qty VARCHAR(MAX),
    product_weight_g VARCHAR(MAX),
    product_length_cm VARCHAR(MAX),
    product_height_cm VARCHAR(MAX),
    product_width_cm VARCHAR(MAX)
);
GO

-- ============================================================================
-- 2. IMPORTATION DU FICHIER CSV DANS LA TABLE STAGING
-- ============================================================================
BULK INSERT dbo.products_staging
FROM 'D:\PROJECTS\AKIENI\DOCUMENTS\RESOURCES\archive\olist_products_dataset.csv'
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
INSERT INTO dbo.products (
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
)
SELECT 
    TRIM(product_id),
    TRIM(product_category_name),
    TRY_CAST(TRIM(product_name_lenght) AS INT),
    TRY_CAST(TRIM(product_description_lenght) AS INT),
    TRY_CAST(TRIM(product_photos_qty) AS INT),
    TRY_CAST(TRIM(product_weight_g) AS INT),
    TRY_CAST(REPLACE(TRIM(product_length_cm), ',', '.') AS DECIMAL(8,2)),
    TRY_CAST(REPLACE(TRIM(product_height_cm), ',', '.') AS DECIMAL(8,2)),
    TRY_CAST(REPLACE(TRIM(product_width_cm), ',', '.') AS DECIMAL(8,2))
FROM dbo.products_staging
WHERE NULLIF(TRIM(product_id), '') IS NOT NULL;
GO

-- ============================================================================
-- 4. NETTOYAGE DE LA TABLE TEMPORAIRE
-- ============================================================================
DROP TABLE dbo.products_staging;
GO