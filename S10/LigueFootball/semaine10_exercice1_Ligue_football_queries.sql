USE LigueFootball;


GO
----------------------------------------------------------
-- PARTIE A : INSERT, UPDATE, DELETE
----------------------------------------------------------
-- Exercice 1 : Insertion de 8 équipes 
INSERT  INTO equipes (
       nom_equipe,
       quartier,
       entraineur,
       annee_creation
)
VALUES              ('AS Poto-Poto', 'Poto-Poto', 'Jean Malonga', 2010),
('FC Bacongo', 'Bacongo', 'Pierre Nzaou', 2008),
('Étoile de Moungali', 'Moungali', 'Serge Loubaki', 2015),
('Ouenzé United', 'Ouenzé', 'Alain Mabiala', 2012),
('Talangaï FC', 'Talangaï', 'Bruno Ngouabi', 2011),
('Makélékélé Sport', 'Makélékélé', 'Rufin Massamba', 2009),
('AS Mfilou', 'Mfilou', 'Claude Ondongo', 2013),
('Djiri Football Club', 'Djiri', 'Fabrice Kimbembe', 2014);


GO
-- Exercice 2a : Insertion de 3 stades 
INSERT  INTO stades (
       nom_stade,
       quartier,
       capacite
)
VALUES             ('Stade Alphonse Massamba-Débat', 'Bacongo', 33000),
('Stade de Kintélé', 'Djiri', 60000),
('Stade Marchand', 'Moungali', 10000);


GO
-- Exercice 2b : Insertion de joueurs par équipe
INSERT  INTO joueurs (
       nom,
       prenom,
       equipe_id,
       poste,
       numero_maillot,
       date_naissance
)
VALUES              -- 1. AS Poto-Poto
('Mboumba', 'Patrick', (SELECT equipe_id
                        FROM   equipes
                        WHERE  nom_equipe = 'AS Poto-Poto'), 'Gardien', 1, '1998-03-12'),
('Kikouama', 'Chardrel', (SELECT equipe_id
                          FROM   equipes
                          WHERE  nom_equipe = 'AS Poto-Poto'), 'Défenseur', 4, '2000-07-25'),
('Mouyabi', 'Glodi', (SELECT equipe_id
                      FROM   equipes
                      WHERE  nom_equipe = 'AS Poto-Poto'), 'Attaquant', 9, '2001-11-05'),
-- 2. FC Bacongo
('Ngatsongo', 'Brudel', (SELECT equipe_id
                         FROM   equipes
                         WHERE  nom_equipe = 'FC Bacongo'), 'Gardien', 16, '1999-01-30'),
('Mpassi', 'Silvère', (SELECT equipe_id
                       FROM   equipes
                       WHERE  nom_equipe = 'FC Bacongo'), 'Milieu', 8, '2002-05-18'),
('Loussoukou', 'Junior', (SELECT equipe_id
                          FROM   equipes
                          WHERE  nom_equipe = 'FC Bacongo'), 'Attaquant', 11, '1997-09-14'),
-- 3. Étoile de Moungali
('Bissiki', 'Magnokélé', (SELECT equipe_id
                          FROM   equipes
                          WHERE  nom_equipe = 'Étoile de Moungali'), 'Défenseur', 2, '1996-12-01'),
('Itoua', 'Béranger', (SELECT equipe_id
                       FROM   equipes
                       WHERE  nom_equipe = 'Étoile de Moungali'), 'Milieu', 6, '2003-04-10'),
('Mokombo', 'Prestige', (SELECT equipe_id
                         FROM   equipes
                         WHERE  nom_equipe = 'Étoile de Moungali'), 'Attaquant', 10, '2000-08-22'),
-- 4. Ouenzé United
('Ndinga', 'Delvin', (SELECT equipe_id
                      FROM   equipes
                      WHERE  nom_equipe = 'Ouenzé United'), 'Milieu', 5, '1995-06-15'),
('Bakaki', 'Hardy', (SELECT equipe_id
                     FROM   equipes
                     WHERE  nom_equipe = 'Ouenzé United'), 'Attaquant', 7, '2001-02-17'),
('Mavoungou', 'Giscard', (SELECT equipe_id
                          FROM   equipes
                          WHERE  nom_equipe = 'Ouenzé United'), 'Gardien', 1, '1998-10-09'),
-- 5. Talangaï FC
('Rozan', 'Varel', (SELECT equipe_id
                    FROM   equipes
                    WHERE  nom_equipe = 'Talangaï FC'), 'Défenseur', 3, '1999-08-11'),
('Niamathé', 'Japhet', (SELECT equipe_id
                        FROM   equipes
                        WHERE  nom_equipe = 'Talangaï FC'), 'Défenseur', 5, '2002-01-03'),
('Gandzé', 'Césaire', (SELECT equipe_id
                       FROM   equipes
                       WHERE  nom_equipe = 'Talangaï FC'), 'Milieu', 10, '1997-03-29'),
-- 6. Makélékélé Sport
('Kipré', 'Zaccharie', (SELECT equipe_id
                        FROM   equipes
                        WHERE  nom_equipe = 'Makélékélé Sport'), 'Gardien', 12, '2000-09-04'),
('Nzaou', 'Prince', (SELECT equipe_id
                     FROM   equipes
                     WHERE  nom_equipe = 'Makélékélé Sport'), 'Milieu', 14, '2003-06-20'),
('Bikoumou', 'Durel', (SELECT equipe_id
                       FROM   equipes
                       WHERE  nom_equipe = 'Makélékélé Sport'), 'Attaquant', 9, '1998-12-25'),
-- 7. AS Mfilou
('Okouri', 'Roland', (SELECT equipe_id
                      FROM   equipes
                      WHERE  nom_equipe = 'AS Mfilou'), 'Attaquant', 11, '2001-07-08'),
('Tsiba', 'Destin', (SELECT equipe_id
                     FROM   equipes
                     WHERE  nom_equipe = 'AS Mfilou'), 'Défenseur', 13, '1999-04-19'),
('Kibongui', 'Arnaud', (SELECT equipe_id
                        FROM   equipes
                        WHERE  nom_equipe = 'AS Mfilou'), 'Milieu', 8, '2002-11-30'),
-- 8. Djiri Football Club
('Nkounkou', 'Pavelh', (SELECT equipe_id
                        FROM   equipes
                        WHERE  nom_equipe = 'Djiri Football Club'), 'Gardien', 1, '1997-05-14'),
('Eboa', 'Christ', (SELECT equipe_id
                    FROM   equipes
                    WHERE  nom_equipe = 'Djiri Football Club'), 'Défenseur', 4, '2000-02-28'),
('Malonga', 'Francel', (SELECT equipe_id
                        FROM   equipes
                        WHERE  nom_equipe = 'Djiri Football Club'), 'Attaquant', 7, '2003-08-16');


GO
-- Exercice 3 : Insertion de 6 matchs de la 1ère journée
INSERT  INTO matchs (
       equipe_domicile_id,
       equipe_exterieur_id,
       stade_id,
       date_match,
       score_domicile,
       score_exterieur
)
VALUES             -- Match 1
((SELECT equipe_id
  FROM   equipes
  WHERE  nom_equipe = 'AS Poto-Poto'), (SELECT equipe_id
                                        FROM   equipes
                                        WHERE  nom_equipe = 'FC Bacongo'), (SELECT stade_id
                                                                            FROM   stades
                                                                            WHERE  nom_stade = 'Stade Alphonse Massamba-Débat'), '2026-09-01', 0, 0),
-- Match 2
((SELECT equipe_id
  FROM   equipes
  WHERE  nom_equipe = 'Étoile de Moungali'), (SELECT equipe_id
                                              FROM   equipes
                                              WHERE  nom_equipe = 'Ouenzé United'), (SELECT stade_id
                                                                                     FROM   stades
                                                                                     WHERE  nom_stade = 'Stade Marchand'), '2026-09-01', 0, 0),
-- Match 3
((SELECT equipe_id
  FROM   equipes
  WHERE  nom_equipe = 'Talangaï FC'), (SELECT equipe_id
                                       FROM   equipes
                                       WHERE  nom_equipe = 'Makélékélé Sport'), (SELECT stade_id
                                                                                 FROM   stades
                                                                                 WHERE  nom_stade = 'Stade de Kintélé'), '2026-09-01', 0, 0),
-- Match 4
((SELECT equipe_id
  FROM   equipes
  WHERE  nom_equipe = 'AS Mfilou'), (SELECT equipe_id
                                     FROM   equipes
                                     WHERE  nom_equipe = 'Djiri Football Club'), (SELECT stade_id
                                                                                  FROM   stades
                                                                                  WHERE  nom_stade = 'Stade Alphonse Massamba-Débat'), '2026-09-01', 0, 0),
-- Match 5
((SELECT equipe_id
  FROM   equipes
  WHERE  nom_equipe = 'AS Poto-Poto'), (SELECT equipe_id
                                        FROM   equipes
                                        WHERE  nom_equipe = 'Étoile de Moungali'), (SELECT stade_id
                                                                                    FROM   stades
                                                                                    WHERE  nom_stade = 'Stade Marchand'), '2026-09-01', 0, 0),
-- Match 6
((SELECT equipe_id
  FROM   equipes
  WHERE  nom_equipe = 'FC Bacongo'), (SELECT equipe_id
                                      FROM   equipes
                                      WHERE  nom_equipe = 'Ouenzé United'), (SELECT stade_id
                                                                             FROM   stades
                                                                             WHERE  nom_stade = 'Stade de Kintélé'), '2026-09-01', 0, 0);


GO
-- Exercice 4 : UPDATE — Enregistrer les résultats 
-- Exercice 4a
UPDATE matchs
SET    score_domicile  = 2,
       score_exterieur = 1
WHERE  match_id = 1;

UPDATE matchs
SET    score_domicile  = 0,
       score_exterieur = 0
WHERE  match_id = 2;

UPDATE matchs
SET    score_domicile  = 3,
       score_exterieur = 2
WHERE  match_id = 3;

UPDATE matchs
SET    score_domicile  = 1,
       score_exterieur = 4
WHERE  match_id = 4;

UPDATE matchs
SET    score_domicile  = 2,
       score_exterieur = 2
WHERE  match_id = 5;

UPDATE matchs
SET    score_domicile  = 1,
       score_exterieur = 0
WHERE  match_id = 6;


GO
-- Exercice 4b : Correction du nom du stade pour le match 1
UPDATE matchs
SET    stade_id = (SELECT stade_id
                   FROM   stades
                   WHERE  nom_stade = 'Stade de Kintélé')
WHERE  match_id = 1;


GO
-- Exercice 5 : Enregistrement des buteurs
INSERT  INTO buts (
       match_id,
       joueur_id,
       minute
)
VALUES           -- Match 1 : AS Poto-Poto (2-1) FC Bacongo
(1, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Glodi'
            AND nom = 'Mouyabi'), 14),
(1, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Chardrel'
            AND nom = 'Kikouama'), 55),
(1, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Junior'
            AND nom = 'Loussoukou'), 82),
-- Match 3 : Talangaï FC (3-2) Makélékélé Sport
(3, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Césaire'
            AND nom = 'Gandzé'), 10),
(3, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Durel'
            AND nom = 'Bikoumou'), 28),
(3, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Varel'
            AND nom = 'Rozan'), 41),
(3, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Césaire'
            AND nom = 'Gandzé'), 67),
(3, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Durel'
            AND nom = 'Bikoumou'), 89),
-- Match 4 : AS Mfilou (1-4) Djiri Football Club
(4, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Roland'
            AND nom = 'Okouri'), 5),
(4, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Francel'
            AND nom = 'Malonga'), 22),
(4, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Francel'
            AND nom = 'Malonga'), 48),
(4, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Christ'
            AND nom = 'Eboa'), 73),
(4, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Francel'
            AND nom = 'Malonga'), 85),
-- Match 5 : AS Poto-Poto (2-2) Étoile de Moungali
(5, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Glodi'
            AND nom = 'Mouyabi'), 33),
(5, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Prestige'
            AND nom = 'Mokombo'), 45),
(5, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Glodi'
            AND nom = 'Mouyabi'), 60),
(5, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Prestige'
            AND nom = 'Mokombo'), 90),
-- Match 6 : FC Bacongo (1-0) Ouenzé United
(6, (SELECT joueur_id
     FROM   joueurs
     WHERE  prenom = 'Junior'
            AND nom = 'Loussoukou'), 76);


GO
-- Exercice 6 : Correction des erreurs de saisie / Doublons
-- Vérification de doublon
SELECT joueur_id,
       nom,
       prenom,
       equipe_id,
       poste
FROM   joueurs
WHERE  nom = 'Mouyabi'
       AND prenom = 'Glodi';


GO
-- Insertion d'un doublon pour le test
INSERT  INTO joueurs (
       nom,
       prenom,
       equipe_id,
       poste,
       numero_maillot,
       date_naissance
)
VALUES              ('Mouyabi', 'Glodi', (SELECT equipe_id
                                          FROM   equipes
                                          WHERE  nom_equipe = 'AS Poto-Poto'), 'Attaquant', 9, '2001-11-05');


GO
-- Suppression du doublon 
DELETE joueurs
WHERE  joueur_id = (SELECT MAX(joueur_id)
                    FROM   joueurs
                    WHERE  nom = 'Mouyabi'
                           AND prenom = 'Glodi');


GO
----------------------------------------------------------
-- PARTIE B : SELECT (Interrogation du championnat)
----------------------------------------------------------
-- Exercice 7a : Nombre d'équipes enregistrées
SELECT COUNT(DISTINCT nom_equipe) AS nombre_equipes_enregistrees
FROM   equipes;


GO
-- Exercice 7b1 : Nombre total des joueurs
SELECT COUNT(*) AS nombre_joueurs_inscrits
FROM   joueurs;


GO
-- Exercice 7b2 : Nombre de joueurs inscrits par équipe
SELECT   equipe_id,
         COUNT(*) AS nombre_joueurs
FROM     joueurs
GROUP BY equipe_id;


GO
-- Exercice 7c : Total des buts de la 1ère journée 
SELECT COUNT(*) AS total_buts_1ere_journee
FROM   buts;


GO
-- Exercice 8a : Tri des joueurs par poste (Attaquants)
SELECT nom,
       prenom,
       equipe_id
FROM   joueurs
WHERE  poste = 'Attaquant';


GO
-- Exercice 8b : Matchs avec plus de 3 buts (cumul extérieur + domicile)
SELECT *
FROM   matchs
WHERE  (score_domicile + score_exterieur) > 3;


GO
-- Exercice 8c : Nombre de joueurs par équipe (du plus petit au plus grand)
SELECT   equipe_id,
         COUNT(*) AS nombre_joueurs
FROM     joueurs
GROUP BY equipe_id
ORDER BY nombre_joueurs ASC;


GO
-- Exercice 8d : Score total de chaque match (du plus au moins spectaculaire)
SELECT   match_id,
         equipe_domicile_id,
         equipe_exterieur_id,
         (score_domicile + score_exterieur) AS total_buts
FROM     matchs
ORDER BY total_buts DESC;