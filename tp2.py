# -*- coding: utf-8 -*-
#!/usr/bin/python


produits = { 1: { 'nom': 'banane', 'prix': 4 }, 2: { 'nom': 'pomme', 'prix': 2 }, 3: { 'nom': 'orange', 'prix': 1.5 }, 4: { 'nom': 'poire', 'prix': 3 } }
for key,value in produits.items():
    print('{}\t | {}\t | {}\t '.format(key,value['nom'],value['prix']))

    # print(key,"\t",value['nom'],"\t", value['prix'])
totalPrixTTC  = 0
totalPrixHT = 0
try:
    np = int(input('Combien de produits ? : '))
except ValueError:
    print("Saisie invalide")
else:
    for i in range(0, np):
        print("produit", i+1)
        try:
            id_produit = int(input('saisir id produit : '))
            qt=float(input('saisir la quantité : '))
        except ValueError:
            print("Id saisie invalide")
        else:
            prixHT=(produits[id_produit]['prix'])*qt
            prixTTC=prixHT*1.20
            totalPrixTTC += prixTTC
            totalPrixHT += prixHT
            remise = 0
            if totalPrixTTC>200:
                remise = totalPrixTTC*5/100
                totalprixTTC=totalPrixTTC*0.95
            print("Prix HT : " ,prixHT)
            print("Prix TTC : ", prixTTC)
            print("Remise : ", remise)
    print("Total Prix HT : " ,totalPrixHT)
    print("Total Prix TTC : ", totalPrixTTC)