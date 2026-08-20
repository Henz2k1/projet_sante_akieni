USE OlistCommerce;
GO

-- ============================================================================
-- 1. CRÉATION DE LA TABLE DE STAGING
-- ============================================================================
IF OBJECT_ID('dbo.customers_staging', 'U') IS NOT NULL
    DROP TABLE dbo.customers_staging;
GO

CREATE TABLE dbo.customers_staging (
    customer_id VARCHAR(MAX),
    customer_unique_id VARCHAR(MAX),
    customer_zip_code_prefix VARCHAR(MAX),
    customer_city VARCHAR(MAX),
    customer_state VARCHAR(MAX)
);
GO

-- ============================================================================
-- 2. IMPORTATION DU FICHIER CSV DANS LA TABLE STAGING
-- ============================================================================
BULK INSERT dbo.customers_staging
FROM 'D:\PROJECTS\AKIENI\DOCUMENTS\RESOURCES\archive\olist_customers_dataset.csv'
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
INSERT INTO dbo.customers (
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state
)
SELECT 
    TRIM(customer_id),
    TRIM(customer_unique_id),
    TRIM(customer_zip_code_prefix),
    TRIM(customer_city),
    TRIM(customer_state)
FROM dbo.customers_staging
WHERE NULLIF(TRIM(customer_id), '') IS NOT NULL;
GO

-- ============================================================================
-- 4. NETTOYAGE DE LA TABLE TEMPORAIRE
-- ============================================================================
DROP TABLE dbo.customers_staging;
GO