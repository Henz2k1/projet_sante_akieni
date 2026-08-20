USE OlistCommerce;
GO

-- ============================================================================
-- 1. CRÉATION DE LA TABLE DE STAGING
-- ============================================================================
IF OBJECT_ID('dbo.order_payments_staging', 'U') IS NOT NULL
    DROP TABLE dbo.order_payments_staging;
GO

CREATE TABLE dbo.order_payments_staging (
    order_id VARCHAR(MAX),
    payment_sequential VARCHAR(MAX),
    payment_type VARCHAR(MAX),
    payment_installments VARCHAR(MAX),
    payment_value VARCHAR(MAX)
);
GO

-- ============================================================================
-- 2. IMPORTATION DU FICHIER CSV DANS LA TABLE STAGING
-- ============================================================================
BULK INSERT dbo.order_payments_staging
FROM 'D:\PROJECTS\AKIENI\DOCUMENTS\RESOURCES\archive\olist_order_payments_dataset.csv'
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
INSERT INTO dbo.order_payments (
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
)
SELECT 
    TRIM(order_id),
    TRY_CAST(TRIM(payment_sequential) AS INT),
    TRIM(payment_type),
    TRY_CAST(TRIM(payment_installments) AS INT),
    TRY_CAST(REPLACE(TRIM(payment_value), ',', '.') AS DECIMAL(10,2))
FROM dbo.order_payments_staging
WHERE NULLIF(TRIM(order_id), '') IS NOT NULL 
  AND NULLIF(TRIM(payment_sequential), '') IS NOT NULL;
GO

-- ============================================================================
-- 4. NETTOYAGE DE LA TABLE TEMPORAIRE
-- ============================================================================
DROP TABLE dbo.order_payments_staging;
GO