# -*- coding: utf-8 -*-
#!/usr/bin/python


produits = { 1: { 'nom': 'banane', 'prix': 4 },2: { 'nom': 'pomme', 'prix': 2 },3: { 'nom': 'orange', 'prix': 1.5 },4: { 'nom': 'poire', 'prix': 3 }  }
print(produits[1]['prix'])


np = int(input('Combien de produits ? : '))
for i in range(0, np):
    print("produit", i+1)
    id_produit = int(input('saisir id produit : '))
    qt=float(input('saisir la quantité : '))
    while id_produit<=0 or qt<=0 :
        print("saisies invalides")
        id_produit = float(input('saisir id produit : '))
        qt=float(input('saisir la quantité : '))
    print(id_produit)
    pht=(produits[id_produit]['prix'])*qt
    pttc=pht*1.20
    if pttc>200:
        pttc=pttc*0.95
    print("Prix TTC : ", pttc)