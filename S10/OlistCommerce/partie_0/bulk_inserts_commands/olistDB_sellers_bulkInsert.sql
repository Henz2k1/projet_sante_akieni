USE OlistCommerce;
GO

-- ============================================================================
-- 1. CRÉATION DE LA TABLE DE STAGING
-- ============================================================================
IF OBJECT_ID('dbo.sellers_staging', 'U') IS NOT NULL
    DROP TABLE dbo.sellers_staging;
GO

CREATE TABLE dbo.sellers_staging (
    seller_id VARCHAR(MAX),
    seller_zip_code_prefix VARCHAR(MAX),
    seller_city VARCHAR(MAX),
    seller_state VARCHAR(MAX)
);
GO

-- ============================================================================
-- 2. IMPORTATION DU FICHIER CSV DANS LA TABLE STAGING
-- ============================================================================
BULK INSERT dbo.sellers_staging
FROM 'D:\PROJECTS\AKIENI\DOCUMENTS\RESOURCES\archive\olist_sellers_dataset.csv'
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
INSERT INTO dbo.sellers (
    seller_id,
    seller_zip_code_prefix,
    seller_city,
    seller_state
)
SELECT 
    TRIM(seller_id),
    TRIM(seller_zip_code_prefix),
    TRIM(seller_city),
    TRIM(seller_state)
FROM dbo.sellers_staging
WHERE NULLIF(TRIM(seller_id), '') IS NOT NULL;
GO

-- ============================================================================
-- 4. NETTOYAGE DE LA TABLE TEMPORAIRE
-- ============================================================================
DROP TABLE dbo.sellers_staging;
GO