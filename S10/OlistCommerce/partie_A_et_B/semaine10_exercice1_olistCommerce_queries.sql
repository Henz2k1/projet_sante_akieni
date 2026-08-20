USE OlistCommerce;
GO

-- ============================================================================
--  PARTIE A : INSERT, UPDATE, DELETE
-- ============================================================================

-- Exercice 1 — Insertion manuelle de données clients
INSERT INTO customers
    (
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state
    )
VALUES
    ('cust_test_001', 'unique_001', '20040', 'Rio de Janeiro-Test', 'RJ'),
    ('cust_test_002', 'unique_002', '01310', 'Sao Paulo-Test', 'SP'),
    ('cust_test_003', 'unique_003', '30130', 'Belo Horizonte-Test', 'MG');


-- Exercice 2 — Insertion conditionnelle avec SELECT 
INSERT INTO order_audit
    (order_id, action_type)
SELECT
    order_id,
    'FLAGGED_CANCEL' AS action_type
FROM orders
WHERE order_status = 'canceled';


-- Exercice 3 — Mises à jour (Correction des données)

-- a) Correction des statuts de livraison pour mars 2018
UPDATE orders 
SET order_status = 'delivered'
WHERE order_status = 'shipped'
    AND order_purchase_timestamp >= '2018-03-01'
    AND order_purchase_timestamp < '2018-04-01';

-- b) Désactivation des produits n'ayant jamais été commandés
UPDATE products
SET is_active = 0
WHERE product_id NOT IN (
    SELECT DISTINCT product_id
FROM order_items
WHERE product_id IS NOT NULL
);


-- Exercice 4 — Suppression et nettoyage

-- a) Suppression des 3 clients fictifs de test
DELETE FROM customers
WHERE customer_id LIKE 'cust_test_%';

-- b) Suppression des avis 5 étoiles sans commentaire
-- Verification préalable de l'impact
SELECT *
FROM order_reviews
WHERE review_score = 5
    AND review_comment_message IS NULL;

SELECT COUNT(*) AS nb_avis_a_supprimer
FROM order_reviews
WHERE review_score = 5
    AND review_comment_message IS NULL;

-- Exécution de la suppression
DELETE FROM order_reviews
WHERE review_score = 5
    AND review_comment_message IS NULL;


-- ============================================================================
--  PARTIE B : SELECT — Requêtes exploratoires
-- ============================================================================

-- Exercice 5 — Exploration de la volumétrie

-- a) Nombre de clients uniques distincts
SELECT COUNT(DISTINCT customer_unique_id) AS nombre_clients_distincts
FROM customers;

-- b) Nombre total de commandes enregistrées
SELECT COUNT(*) AS nombre_commandes
FROM orders;

-- c) Nombre de produits distincts vendus au moins une fois
SELECT COUNT(DISTINCT product_id) AS produits_distincts_vendus
FROM order_items;

-- d) Nombre de vendeurs enregistrés
SELECT COUNT(*) AS nombre_vendeurs
FROM sellers;


-- Exercice 6 — Filtrage des données avec WHERE

-- a) Liste des commandes annulées
SELECT
    order_id,
    customer_id,
    order_purchase_timestamp
FROM orders
WHERE order_status = 'canceled';

-- b) Identification des produits hors gabarit (> 10 kg)
SELECT
    product_id,
    product_category_name,
    product_weight_g
FROM products
WHERE product_weight_g > 10000;

-- c) Nombre de commandes passées au 1er semestre 2018 (du 1er jan. au 30 juin)
SELECT COUNT(*) AS commandes_premier_semestre_2018
FROM orders
WHERE order_purchase_timestamp >= '2018-01-01'
    AND order_purchase_timestamp < '2018-07-01';


-- Exercice 7 — Tri et limitation des résultats

-- a) Top 10 des articles vendus les plus chers
SELECT TOP 10
    order_id,
    product_id,
    price
FROM order_items
ORDER BY price DESC;

-- b) Aperçu des 15 dernières commandes passées (les plus récentes)
SELECT TOP 15
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp
FROM orders
ORDER BY order_purchase_timestamp DESC;


-- Exercice 8 — Agrégations avec GROUP BY

-- a) Répartition du nombre de commandes par statut
SELECT
    order_status,
    COUNT(*) AS nombre_commandes
FROM orders
GROUP BY order_status
ORDER BY nombre_commandes DESC;

-- b) Top 5 des États brésiliens comptant le plus de clients
SELECT TOP 5
    customer_state,
    COUNT(*) AS nombre_clients
FROM customers
GROUP BY customer_state
ORDER BY nombre_clients DESC;

-- c) Prix moyen, minimum et maximum par vendeur (ayant plus de 20 ventes)
SELECT
    seller_id,
    AVG(price) AS prix_moyen,
    MIN(price) AS prix_minimum,
    MAX(price) AS prix_maximum
FROM order_items
GROUP BY seller_id
HAVING COUNT(*) > 20;


-- Exercice 9 — Utilisation des fonctions de date

-- a) Top 20 des délais de livraison les plus longs (en jours)
SELECT TOP 20
    order_id,
    order_purchase_timestamp,
    order_delivered_customer_date,
    DATEDIFF(
        DAY,
        order_purchase_timestamp,
        order_delivered_customer_date
    ) AS delai_livraison_jours
FROM orders
WHERE order_status = 'delivered'
    AND order_delivered_customer_date IS NOT NULL
ORDER BY delai_livraison_jours DESC;

-- b) Nombre de commandes par mois (trié par volume décroissant)
SELECT
    YEAR(order_purchase_timestamp) AS annee,
    MONTH(order_purchase_timestamp) AS mois,
    COUNT(*) AS nombre_commandes
FROM orders
GROUP BY
    YEAR(order_purchase_timestamp),
    MONTH(order_purchase_timestamp)
ORDER BY nombre_commandes DESC;


-- Exercice 10 — Analyse financière et des moyens de paiement

-- a) Analyse des transactions et montants par type de paiement
SELECT
    payment_type,
    COUNT(*) AS nombre_transactions,
    SUM(payment_value) AS total_encaisse,
    AVG(payment_value) AS montant_moyen
FROM order_payments
GROUP BY payment_type
ORDER BY total_encaisse DESC;

-- b) Nombre de commandes ayant utilisé plusieurs modes de paiement
SELECT COUNT(DISTINCT order_id) AS commandes_avec_plusieurs_paiements
FROM order_payments
WHERE payment_sequential > 1;

-- c) Chiffre d'affaires mensuel basé sur la table order_items (sans jointure)
SELECT
    YEAR(shipping_limit_date) AS annee,
    MONTH(shipping_limit_date) AS mois,
    FORMAT(shipping_limit_date, 'yyyy-MM') AS annee_mois,
    SUM(price) AS chiffre_affaires_total
FROM order_items
GROUP BY 
    YEAR(shipping_limit_date),
    MONTH(shipping_limit_date),
    FORMAT(shipping_limit_date, 'yyyy-MM')
ORDER BY 
    annee ASC, 
    mois ASC;