def somme_nombres_pairs(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme

# Exemple d'utilisation :
ma_liste = [1, 2, 3, 4,5]
resultat = somme_nombres_pairs(ma_liste)
print("La somme des nombres pairs dans la liste est :", resultat)
