USE OlistCommerce;
GO

-- ============================================================================
-- ÉTAPE 1 : RECRÉATION DE LA TABLE CIBLE AVEC CLÉ PRIMAIRE COMPOSÉE
-- ============================================================================
IF OBJECT_ID('dbo.order_reviews', 'U') IS NOT NULL
    DROP TABLE dbo.order_reviews;
GO

CREATE TABLE dbo.order_reviews
(
    review_id VARCHAR(50) NOT NULL,
    order_id VARCHAR(50) NOT NULL,
    review_score INT NULL,
    review_comment_title NVARCHAR(MAX) NULL,
    review_comment_message NVARCHAR(MAX) NULL,
    review_creation_date DATETIME2 NULL,
    review_answer_timestamp DATETIME2 NULL,

    -- Clé primaire composée garantissant l'unicité des 99 224 lignes
    CONSTRAINT PK_order_reviews PRIMARY KEY (review_id, order_id)
);
GO

-- ============================================================================
-- ÉTAPE 2 : PRÉPARATION DE LA TABLE DE STAGING (TEMPORAIRE)
-- ============================================================================
IF OBJECT_ID('dbo.order_reviews_staging', 'U') IS NOT NULL
    DROP TABLE dbo.order_reviews_staging;
GO

CREATE TABLE dbo.order_reviews_staging
(
    review_id NVARCHAR(MAX),
    order_id NVARCHAR(MAX),
    review_score NVARCHAR(MAX),
    review_comment_title NVARCHAR(MAX),
    review_comment_message NVARCHAR(MAX),
    review_creation_date NVARCHAR(MAX),
    review_answer_timestamp NVARCHAR(MAX)
);
GO

-- ============================================================================
-- ÉTAPE 3 : IMPORTATION BRUTE DU CSV DANS LA STAGING (BULK INSERT)
-- ============================================================================
BULK INSERT dbo.order_reviews_staging
FROM 'D:\PROJECTS\AKIENI\DOCUMENTS\RESOURCES\archive\olist_order_reviews_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,             -- Ignore la ligne d'en-tête
    FIELDQUOTE = '"',         -- Gère les guillemets autour des textes
    FIELDTERMINATOR = ',',     -- Séparateur de colonnes (virgule)
    ROWTERMINATOR = '0x0d0a', -- Fin de ligne Windows (\r\n)
    CODEPAGE = '65001',       -- Encodage UTF-8
    TABLOCK
);
GO

-- ============================================================================
-- ÉTAPE 4 : NETTOYAGE, TYPAGE ET INSERTION DANS LA TABLE FINALE
-- ============================================================================
INSERT INTO dbo.order_reviews
    (
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_comment_message,
    review_creation_date,
    review_answer_timestamp
    )
SELECT
    TRIM(review_id),
    TRIM(order_id),
    TRY_CAST(TRIM(review_score) AS INT),
    NULLIF(TRIM(review_comment_title), ''), -- Transforme les chaînes vides en NULL
    NULLIF(TRIM(review_comment_message), ''), -- Transforme les chaînes vides en NULL
    TRY_CAST(TRIM(review_creation_date) AS DATETIME2),
    TRY_CAST(TRIM(review_answer_timestamp) AS DATETIME2)
FROM dbo.order_reviews_staging
WHERE NULLIF(TRIM(review_id), '') IS NOT NULL;
GO

-- ============================================================================
-- ÉTAPE 5 : SUPPRESSION DU STAGING
-- ============================================================================
DROP TABLE dbo.order_reviews_staging;
GO
