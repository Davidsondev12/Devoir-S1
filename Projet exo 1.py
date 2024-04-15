def afficher_instructions():
    print("Instructions pour entrer les expressions booléennes :")
    print("- Utilisez 'and', 'or', 'not', et 'xor' pour les opérateurs logiques.")
    print("- Pour préciser l'ordre des opérations, entourez les opérations prioritaires avec des parenthèses.")
    print("Exemple : (a and b) or (c and (not d))")

def trouver_variables(expression):
    expression = expression.replace("xor", "").replace("and", "").replace("or", "").replace("not", "").replace(" ", "")
    variables = {char for char in expression if char.isalpha()}
    return sorted(variables)

def formater_expression(expression):
    formatted_expression = (expression.replace("and", " and ")
                            .replace("xor", "^")
                            .replace("not", " not ")
                            .replace("or", " or "))
    return formatted_expression

def evaluer_expression(expression, valeurs_variables, variables):
    env = {var: int(val) for var, val in zip(variables, valeurs_variables)}
    expression_python = expression.replace("and", " and ").replace("or", " or ").replace("not ", " not ").replace("xor", "^")
    return int(eval(expression_python, {"__builtins__": None}, env))

def generer_table_verite_et_formes_canoniques(expression):
    variables = trouver_variables(expression)
    formatted_expression = formater_expression(expression)
    table_verite = []
    print(' | '.join(variables) + ' | Résultat')
    
    for i in range(2**len(variables)):
        valeurs_variables = [(i >> j) & 1 for j in range(len(variables)-1, -1, -1)]
        resultat = evaluer_expression(formatted_expression, valeurs_variables, variables)
        print(' | '.join(map(str, valeurs_variables)) + ' | ' + str(resultat))
        table_verite.append(valeurs_variables + [resultat])

    sop = forme_sop(variables, table_verite)
    pos = forme_pos(variables, table_verite)
    print("\nForme SOP (Somme de Produits):", sop)
    print("Forme POS (Produit de Sommes):", pos)

def forme_sop(variables, table_verite):
    termes = []
    for ligne in table_verite:
        if ligne[-1] == 1:
            terme = []
            for var, val in zip(variables, ligne[:-1]):
                terme.append(var if val else f"{var}'")
            termes.append(''.join(terme))
    return ' + '.join(termes) if termes else "0"

def forme_pos(variables, table_verite):
    termes = []
    for ligne in table_verite:
        if ligne[-1] == 0:
            terme = []
            for var, val in zip(variables, ligne[:-1]):
                terme.append(f"{var}'" if val else var)
            termes.append('(' + ' + '.join(terme) + ')')
    return ' * '.join(termes) if termes else "1"

# Code principal
afficher_instructions()
expression_input = input("Entrez la fonction booléenne (utilisez and, or, not, xor) : ")
generer_table_verite_et_formes_canoniques(expression_input)

