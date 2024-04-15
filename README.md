# Devoir-S1
Information sur le code:

1. **Afficher les instructions**
   - Affiche les instructions pour l'utilisateur sur comment entrer les expressions booléennes, incluant les opérateurs logiques et l'utilisation des parenthèses pour contrôler l'ordre des opérations.

2. **Trouver les variables dans une expression**
   - Supprime les mots-clés logiques et les espaces de l'expression.
   - Extrait les caractères alphabétiques uniques (les variables) et les retourne triés.

3. **Formater l'expression booléenne**
   - Remplace les mots-clés logiques par des formats appropriés pour une évaluation en Python (par exemple, "xor" par "^").
   - Ajoute des espaces autour de certains opérateurs pour éviter les erreurs d'interprétation.

4. **Évaluer l'expression booléenne**
   - Convertit les valeurs des variables en entiers (0 ou 1).
   - Construit un environnement d'évaluation avec ces valeurs.
   - Évalue l'expression formatée en utilisant cet environnement.
   - Retourne le résultat de l'évaluation sous forme d'entier.

5. **Générer la table de vérité et les formes canoniques**
   - Trouve les variables utilisées dans l'expression.
   - Formate l'expression pour l'évaluation.
   - Itère sur toutes les combinaisons possibles de valeurs de vérité pour les variables.
   - Pour chaque combinaison, évalue l'expression et affiche le résultat.
   - Calcule et affiche la Forme Canonique Somme de Produits (SOP) et la Forme Canonique Produit de Sommes (POS) basées sur la table de vérité.

6. **Calculer la forme SOP**
   - Pour chaque ligne de la table de vérité où le résultat est 1, construit un terme pour la somme de produits.
   - Chaque variable est accompagnée de son complément si sa valeur est 0 dans cette ligne.
   - Concatène tous les termes pour former l'expression SOP.

7. **Calculer la forme POS**
   - Pour chaque ligne de la table de vérité où le résultat est 0, construit un terme pour le produit de sommes.
   - Chaque variable est accompagnée de son complément si sa valeur est 1 dans cette ligne.
   - Concatène tous les termes pour former l'expression POS.

8. **Exécuter le programme**
   - Affiche les instructions.
   - Demande à l'utilisateur d'entrer une expression booléenne.
   - Appelle la fonction pour générer la table de vérité et les formes canoniques de l'expression entrée.

Ce flux de traitement fournit une approche structurée pour analyser et évaluer les expressions booléennes, utile pour des applications telles que la conception de circuits logiques ou l'enseignement des concepts de logique booléenne.
