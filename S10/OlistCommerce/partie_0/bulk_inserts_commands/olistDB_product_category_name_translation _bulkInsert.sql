USE OlistCommerce;
GO

-- ============================================================================
-- 1. CRÉATION DE LA TABLE DE STAGING
-- ============================================================================
IF OBJECT_ID('dbo.product_category_name_translation_staging', 'U') IS NOT NULL
    DROP TABLE dbo.product_category_name_translation_staging;
GO

CREATE TABLE dbo.product_category_name_translation_staging (
    product_category_name VARCHAR(MAX),
    product_category_name_english VARCHAR(MAX)
);
GO

-- ============================================================================
-- 2. IMPORTATION DU FICHIER CSV DANS LA TABLE STAGING
-- ============================================================================
BULK INSERT dbo.product_category_name_translation_staging
FROM 'D:\PROJECTS\AKIENI\DOCUMENTS\RESOURCES\archive\product_category_name_translation.csv'
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
INSERT INTO dbo.product_category_name_translation (
    product_category_name,
    product_category_name_english
)
SELECT 
    TRIM(product_category_name),
    TRIM(product_category_name_english)
FROM dbo.product_category_name_translation_staging
WHERE NULLIF(TRIM(product_category_name), '') IS NOT NULL;
GO

-- ============================================================================
-- 4. NETTOYAGE DE LA TABLE TEMPORAIRE
-- ============================================================================
DROP TABLE dbo.product_category_name_translation_staging;
GO