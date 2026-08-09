

-- Exercice 1
CREATE DATABASE LigueFootball;
GO

USE LigueFootball;
GO

-- Exercice 2 
CREATE TABLE equipes (
    equipe_id INT IDENTITY(1,1) PRIMARY KEY,
    nom_equipe VARCHAR(50) NOT NULL,
    quartier VARCHAR(50) NOT NULL,
    entraineur VARCHAR(50),
    annee_creation INT
);
GO

CREATE TABLE stades (
    stade_id INT IDENTITY(1,1) PRIMARY KEY,
    nom_stade VARCHAR(50) NOT NULL,
    quartier VARCHAR(50),
    capacite INT
);
GO

-- Exercice 3 
CREATE TABLE joueurs (
    joueur_id INT IDENTITY(1,1) PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    equipe_id INT FOREIGN KEY REFERENCES equipes(equipe_id),
    poste VARCHAR(20) NOT NULL,
    numero_maillot INT,
    date_naissance DATE
);
GO

CREATE TABLE matchs (
    match_id INT IDENTITY(1,1) PRIMARY KEY,
    equipe_domicile_id INT FOREIGN KEY REFERENCES equipes(equipe_id),
    equipe_exterieur_id INT FOREIGN KEY REFERENCES equipes(equipe_id),
    stade_id INT FOREIGN KEY REFERENCES stades(stade_id),
    date_match DATE NOT NULL,
    score_domicile INT DEFAULT 0,
    score_exterieur INT DEFAULT 0
);
GO

CREATE TABLE buts (
    but_id INT IDENTITY(1,1) PRIMARY KEY,
    match_id INT FOREIGN KEY REFERENCES matchs(match_id),
    joueur_id INT FOREIGN KEY REFERENCES joueurs(joueur_id),
    minute INT
);
GO

-- Exercice 4
ALTER TABLE joueurs
ADD CHECK (poste IN ('Gardien', 'Défenseur', 'Milieu', 'Attaquant'));
GO

-- Exercice 5
ALTER TABLE matchs
ADD diff_buts AS (score_domicile - score_exterieur);
GO

-- Exercice 6
ALTER TABLE joueurs
ADD capitaine BIT DEFAULT 0,
    telephone VARCHAR(20);
GO

-- Exercice 7
CREATE TABLE test_saison_1 (
    saison_id INT IDENTITY(1,1) PRIMARY KEY,
    nom_saison VARCHAR(50),
    annee INT
);
GO

EXEC sp_rename 'test_saison_1', 'test_saison_2';
GO

DROP TABLE test_saison_2;
GO

-- Exercice 8a
CREATE INDEX IX_matchs_date_match 
ON matchs(date_match);
GO

-- Exercice 8b
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_CATALOG = 'LigueFootball'
ORDER BY TABLE_NAME, ORDINAL_POSITION;
GO