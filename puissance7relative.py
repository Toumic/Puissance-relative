#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Puissance ultime
""" Procédé de mise à niveau de l'exposant"""
# Music@toumic:     puissance7relative.py
print("""Puissance(ex) Relative:\n Commun(n1) = Nombre(n2)**(ex)
    L'exposant est basique
""")


def stage(ult):
    """Part de l'exposant(ex) sur nombre(n2)  
    pour une approche de la valeur(n1(ult))
        (ex) = exposant | (n1) = (n2) ** (ex)"""
    # pour(' *NIVELE*', ult)
    imagee = {2: "BIEN"}  # Détecte l'interminable
    memore = {}  # Mémoire ponctuelle
    pointe = 0.0  # Zéro et Réel
    exp = [.1]  # Un décimal
    but = 3  # Niveau décimal
    www = 0
    # Exposé décimal
    while imagee[2] == "BIEN":
        www += 1
        pas = ima = 0
        while 1:
            # if www > 3: imagee[2] == "STOP"; break
            pointe += exp[0]  # Décimale ajoutée
            copiee = str(pointe)  # Image de forme
            collee = float(copiee[:but])  # Forme
            puisse = (nombre ** collee).real
            expose = puisse - ult
            # print(www, 'Wcollee=',collee,';ult=',ult)
            # print('Wpuisse=',puisse,';ult=',ult)
            # print('WnbrEp =',(nombre**puisse).real)
            if ima == 0:
                imagee[1] = collee
                imagee[3] = expose
                ima = 1
                # print(www, 'WI expose', expose, 'puisse', puisse, 'pas', pas)
            # Nombre négatif = complex(puissance)
            if expose < 0.0 and imagee[2] == "BIEN":
                memore[0] = collee
                pas += 1
                #if (puisse - ult) != 0.0: print('', expose, ult)
                if pas > 10:  # Détecte l'interminable
                    if imagee[1] == memore[0] \
                            or imagee[3] == expose:
                        imagee[2] = "STOP"
                        print(www, 'IIOpas', imagee[2], pas)
            elif expose == 0.0:  # Zéro égal expose
                memore[0] = collee
                imagee[2] = "STOP"
                refute[ult] = [collee, puisse]
                print(www, 'ELzero', imagee[2])
                break
            else:  # Puissance expose
                # Relance machine (Si, nombre**0.1 > ult)
                if puisse > ult and collee == 0.1:
                    print(www, 'Rexp', exp[0], ult)
                    # Mises à niveaux
                    while puisse.real > ult:
                        but += 1
                        exp[0] /= 10
                        puisse = nombre ** exp[0]
                        #print('Rmotor', puisse, ult)                       
                    pointe = exp[0]
                    collee = pointe
                    print(www, 'Rcollee', collee)
                    print('Relance', pointe, puisse, exp[0], 'pas', pas)
                else:
                    refute[ult] = [collee, puisse]
                    # print('STOPrefute', refute[ult])
                    break
        if memore:
            # Mises à niveaux
            pointe = memore[0]
            exp[0] /= 10  # Décimale ajoutée
            but += 1  # Mise en forme
            # print(www, 'Mises à niveaux')
        else:
            memore[0] = pointe
            print(www, 'IE pointe', pointe, 'pas', pas)
            break
    if memore:
        etagee[ult] = memore[0]
        print('           memore', memore)


etagee = {}
refute = {}

# Appel stage
nivele = [2154999]  # nivele supérieur à 0
nombre = -37321  # nombres impuissants (0,1)
print(' nOmbre = {} ; typO = {}\n nIvele = {} ; typI = {}'.
      format(nombre, nombre % 6, nivele[0], nivele[0] % 6))
for ni in nivele:
    if ni > 0:  # Solution provisoire
        stage(ni)
    else:
        print('Inférieur à zéro refusé')

print('etagee', etagee)
# Stage relate
for et, it in etagee.items():
    if it < 1.0:
        print('exINF = {} ; n2ex = {}'.format(it, (nombre ** it).real))
    else:
        print('eXSUP = {} ; n2ex = {}'.format(it, (nombre ** it).real))
    # print(' refute = {}'. format(refute[et]))

# Remarques:
"""Le résultat n'est pas justifié
Exemple(n1 = 32541):
    exINF = 0.4818585027866879
    nombre = 2315468792
        n2ex = nombre ** exINF
        n1 - n2ex = 7.639755494892597e-11
        ..."""
# Stage négatif
"""Nombre négatif accepté
    Nombre nivele refusé, en cours
Nombre négatif: OUI
     nOmbre = -231546 ; typO = 0
     nIvele = 546 ; typI = 0
    eXSUP = 1.500001559834342 ; n2ex = 545.9999998981401
Nivele négatif: NON
     nOmbre = 231546 ; typO = 0
     nIvele = -546 ; typI = 0
    exINF = -546 ; n2ex = 0.0
"""
# Stage complate
"""Le type est un indice
    La famille type's donne une mesure en plus
    Le typO ou le nombre à mettre en puissance
 nOmbre = 231684 ; typO = 0
    Le typI ou le point d'arrivée du nombre
 nIvele = 322564854120055 ; typI = 1
    Le typX ou l'exposant à son terme
eXSUP = 2.704361264537945 ; typX = 2.704361264537945
    Le typ2 ou la solution de type remarquable
n2ex = 322564854120052.0 ; typ2 = 4.0
 refute = [2.704361264537945, 322564854120052.0]  
"""
"""
2**-3 ou 1/2**3
"""
# Court exposé
"""
"""
# f
