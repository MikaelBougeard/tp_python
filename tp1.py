# -*- coding: utf-8 -*-
#!/usr/bin/python
np = int(input('Combien de produits ? : '))
for i in range(0, np):
    print("produit", i+1)
    pht = float(input('saisir prix hors taxe : '))
    qt=float(input('saisir la quantité : '))
    while pht<=0 or qt<=0 :
        print("saisies invalides")
        pht = float(input('saisir prix hors taxe : '))
        qt=float(input('saisir la quantité : '))
    ptc=pht*qt*0.8
    print("Prix TTC : ", ptc)