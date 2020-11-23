# -*- coding: utf-8 -*-
#!/usr/bin/python

id = [1,2,3,5]
nom = ["bannane","pomme","orange","poire"]
prix = [4,2,1.5,3]


np = int(input('Combien de produits ? : '))
for i in range(0, np):
    print("produit", i+1)
    pht = int(input('saisir id produit : '))
    qt=float(input('saisir la quantité : '))
    while pht<=0 or qt<=0 :
        print("saisies invalides")
        pht = float(input('saisir id produit : '))
        qt=float(input('saisir la quantité : '))
    ptc=float(prix[pht-1]*qt*1.2)
    if ptc>200:
        ptc=ptc*0.95
    print("Prix TTC : ", ptc)