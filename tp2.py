# -*- coding: utf-8 -*-
#!/usr/bin/python

produits = { 1: { 'nom': 'banane', 'prix': 4 }, 2: { 'nom': 'pomme', 'prix': 2 }, 3: { 'nom': 'orange', 'prix': 1.5 }, 4: { 'nom': 'poire', 'prix': 3 } }

def remise(a) :
    if a>200:
        b = a*0.95
        return b
    else:
        return a

def tva(a) :
    return a * 1.20

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
        print("Produit numéro ", i+1)
        try:
            id = int(input('saisir id produit : '))
            quantite = float(input('saisir la quantité : '))
        except ValueError:
            print("Id ou quantité saisie invalide")
        else:
            prixHT=(produits[id]['prix'])*quantite
            srPrixHT = prixHT
            prixHT= remise(prixHT)
            prixTTC= tva(prixHT)

            totalPrixTTC += prixTTC
            totalPrixHT += prixHT

            print("Prix TTC Produit(s) : ", srPrixHT)
            if srPrixHT>200 :
                print("Remise 5% : ", prixHT*5/100)
            print("Total Prix HT Produit(s) : ","%.2f" % prixHT)
            print("Total Prix TTC Produit(s) : ","%.2f" % prixTTC)

    print("Total Prix HT : " ,"%.2f" % totalPrixHT)
    print("Total Prix TTC : ","%.2f" % totalPrixTTC)
