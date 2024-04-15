def implicant_premier(term_arr):
    """
    Trouve les implicants premiers à partir d'une liste de termes.
    """
    return_arr = []
    for term1 in term_arr:
        for term2 in term_arr:
            if term1 != term2:
                similar_indexes = [idx for idx in range(len(term1)) if term1[idx] == term2[idx]]
                if len(term1) - len(similar_indexes) <= 1:
                    tmp = combine(term1, term2)
                    if tmp not in return_arr:
                        return_arr.append(tmp)
    return return_arr


def combine(implicant1, implicant2):
    """
    Combine deux implicants en remplaçant les valeurs différentes par un "-".
    """
    return_arr = []
    for idx in range(len(implicant1)):
        if implicant1[idx] == implicant2[idx]:
            return_arr.append(implicant1[idx])
        else:
            return_arr.append("-")
    return return_arr


def est_derive(a, b):
    """
    Vérifie si l'implicant 'a' peut être dérivé de l'implicant 'b'.
    """
    for bit_idx in range(len(a)):
        if a[bit_idx] != b[bit_idx] and a[bit_idx] != "-":
            return False
    return True


def supp_redondance(term_arr):
    """
    Supprime les redondances dans une liste d'implicants.
    """
    new_list = []
    for term1_idx in range(len(term_arr)):
        if term_arr[term1_idx] not in new_list:
            new_list.append(term_arr[term1_idx])
    indexes_to_remove = []
    for term1_idx in range(len(new_list)):
        for term2_idx in range(len(new_list)):
            if term1_idx != term2_idx and est_derive(new_list[term1_idx], new_list[term2_idx]):
                indexes_to_remove.append(term2_idx)
    indexes_to_remove = list(dict.fromkeys(indexes_to_remove))
    indexes_to_remove.sort()
    for idx in reversed(range(len(indexes_to_remove))):
        del new_list[indexes_to_remove[idx]]
    return new_list


def colonne(prime_implicant):
    """
    Crée les colonnes du tableau de couverture avec les implicants premiers.
    """
    if "-" not in prime_implicant:
        return [prime_implicant]
    col = []
    idx = prime_implicant.index("-")
    for bit in ['0', '1']:
        tmp = prime_implicant.copy()
        tmp[idx] = bit
        arr = colonne(tmp)
        for k in arr:
            col.append(k)
    return col


def tableau_redondance(minterms):
    """
    Crée le tableau de couverture avec les mintermes donnés.
    """
    chart = []
    for i in range(len(minterms)):
        chart.append(colonne(minterms[i]))
    return chart


def minterme_tableau(chart):
    """
    Renvoie tous les mintermes présents dans le tableau de couverture.
    """
    all_minterms = []
    for row in chart:
        for item in row:
            if item not in all_minterms:
                all_minterms.append(item)
    return all_minterms


def convertir_string(minterms, var_list):
    """
    Convertit les mintermes en une chaîne de caractères représentant la fonction booléenne.
    """
    output = ''
    for minterm in minterms:
        for bit_idx in range(len(minterm)):
            if minterm[bit_idx] != "-":
                output += '(' + var_list[bit_idx] + ')' if len(var_list) > 1 else var_list[bit_idx]
                output += "!" if minterm[bit_idx] == '0' else ''
                output += "." if bit_idx < len(minterm) - 1 else ''
        output += " + " if minterm != minterms[-1] else ""
    return output


def factoriser(minterms, var_list):
    """
    Factorise les implicants premiers communs.
    """
    common = ["-"] * len(minterms[0])
    if len(minterms) > 1:
        for bit in range(len(minterms[0])):
            for term in range(1, len(minterms)):
                if minterms[0][bit] != minterms[term][bit] or minterms[term][bit] == "-":
                    break
                elif term == len(minterms) - 1:
                    common[bit] = minterms[term][bit]
                    for k in range(len(minterms)):
                        minterms[k][bit] = "-"
    common = convertir_string([common], var_list)
    return common


def simplifier(minterms, var_list=[]):
    """
    Simplifie une fonction booléenne à partir de ses mintermes.
    """
    if len(minterms) == 0:
        raise Exception("Nombre insuffisant de mintermes")
    
    # Déterminer le nombre de variables
    var_count = len(bin(max(minterms))) - 2
    
    # Générer une liste de variables si non fournie
    if len(var_list) == 0:
        var_list = list(map(chr, range(65, 65 + var_count)))
    elif len(var_list) < var_count:
        raise Exception("Nombre insuffisant de variables")
    
    # Convertir les mintermes en binaire
    for i in range(len(minterms)):
        minterms[i] = list(bin(int(minterms[i]))[2:].zfill(var_count))

    # Trouver les implicants premiers
    prime_implicants = implicant_premier(minterms)
    
    # Générer la liste complète des implicants
    while len(prime_implicants) != 0:
        for prime_implicant in prime_implicants:
            minterms.append(prime_implicant)
        prime_implicants = implicant_premier(prime_implicants)

    # Supprimer les redondances
    minterms = supp_redondance(minterms)

    # Créer le tableau de couverture
    chart = tableau_redondance(minterms)
    all_minterms = sorted(minterme_tableau(chart))

    # Factoriser les implicants premiers communs
    multiples = factoriser(minterms, var_list)

    # Convertir en chaîne de caractères
    output = convertir_string(minterms, var_list)

    if multiples:
        output = multiples + "." + '(' + output + ')'
    return output


def liste_variables(fonc):
    """
    Renvoie la liste des variables présentes dans la fonction booléenne.
    """
    return sorted(set(filter(str.isalpha, fonc)))


def evaluer(fonc, var_dict):
    """
    Évalue la fonction booléenne pour un ensemble de valeurs de variables.
    """
    fonc = fonc.replace("+", " or ")
    fonc = fonc.replace(".", " and ")
    fonc = fonc.replace("!", " not ")

    for variable, value in var_dict.items():
        fonc = fonc.replace(variable, str(value))

    return eval(fonc)


def mintermes(fonc):
    """
    Trouve les mintermes de la fonction booléenne donnée.
    """
    fonc = fonc.upper()

    resultats = []
    var = liste_variables(fonc)
    var_count = len(var)

    tab = []
    for i in range(2 ** var_count):
        b = list(bin(i)[2:].zfill(var_count))
        tab.append(b)

    for i in range(len(tab)):
        value_dict = dict(zip(var, tab[i]))
        result = evaluer(fonc, value_dict)
        if result:
            resultats.append(i)

    return resultats, var


def main():
    fonc = input("Veuillez entrer la fonction booléenne à minimiser (utilisez les opérateurs logiques 'and', 'or', 'not', et les variables en majuscules) : ")
    resultats, var = mintermes(fonc)
    print("Fonction minimale:\n\t", simplifier(resultats, var))


if __name__ == "__main__":
    main()
    