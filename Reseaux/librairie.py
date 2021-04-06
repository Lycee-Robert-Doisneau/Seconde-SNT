#!/usr/bin/python
# -*- coding: utf-8 -*-

# ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
# ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
#     ╒ ╕ ╘ ╛ ╞ ╡ ╤ ╧ ╪
#     ╓ ╖ ╙ ╜ ╟ ╢ ╥ ╨ ╫


#!/usr/bin/python
# -*- coding: utf-8 -*-


## introduction
def nettoyage(saisie):
    temp = ""
    for c in saisie.lower():
        if c in "éèêë": temp += "e"
        elif c in 'àâ': temp += "a"
        elif c in "ôö": temp += "o"
        elif c in "îï": temp += "i"
        elif c in "ùûü": temp += "u"
        elif c in "ç": temp += "c"
        elif c in "abcedfghijklmnopqrstuvwxyz0123456789": temp += c
    return temp

def activite1_ex1():
    noeuds = ['box','telephone','cpl','televiseurboitier','ordinateurfixe','ordinateurportable']
    histo = []
    while len(noeuds) > 0:
        saisie = nettoyage(input(f"-Proposer un noeud du réseau domestique (chez vous) (Reste à trouver {len(noeuds)}): "))
        if saisie in noeuds:
            histo.append(saisie)
            noeuds.remove(saisie)
            print(f"Bravo!\n")
        else:
            if saisie in histo: print("Déjà proposé\n")
            else: print("Raté! (veillez à l'orthographe)\n")    
    print("\nFélicitations!!!")

def activite1_ex2():
    noeuds = ['cablerj45','cablerj11','wifi']
    histo = []
    while len(noeuds) > 0:
        saisie = nettoyage(input(f"-Proposer un noeud du réseau domestique (chez vous) (Reste à trouver {len(noeuds)}): "))
        if saisie in noeuds:
            histo.append(saisie)
            noeuds.remove(saisie)
            print(f"Bravo!\n")
        else:
            if saisie in histo: print("Déjà proposé\n")
            else: print("Raté! (veillez à l'orthographe)\n")    
    input("Remarque: il existe aussi une liaison entre deux nœuds CPL, les données circulent ici dans le réseau électrique (prises murales).\nAppuyer sur Entrée pour valider.")
    print("Félicitations!!!")

def activite1_ex3():
    total = 0
    print(f"Situation n°1: Vous regardez la télévision captée sur internet\n{62*'-'}")
    print("1) Internet > Box > Câble RJ45 > CPL > réseau élec. > CPL > Câble RJ45 > Téléviseur+Boîtier")
    print("2) Internet > Box > Câble RJ45 > Wi-Fi > Téléviseur+Boîtier")
    print("3) CPL > réseau élec. > CPL > Câble RJ45 > Téléviseur+Boîtier")
    print("4) Box > Câble RJ45 > CPL > réseau élec. > CPL > Câble RJ45 > Téléviseur+Boîtier")
    reponse = " "
    while reponse not in "1234": 
        reponse = input("\nRéponse à la situation n°1: ")
        if reponse in "1234":
            if reponse == "1":
                print("Bravo!")
                total += 1
            else:
                print("Dommage!")
        else: print("Réponse inexistante")
    
    print(f"Situation n°2: Vous consultez un site internet sur votre ordinateur portable\n{76*'-'}")
    print("1) Internet > Box > Câble RJ45 > Ordinateur portable")
    print("2) Internet > Box > Wi-Fi > Ordinateur portable")
    print("3) Internet > CPL > réseau élec. > CPL > Box > Ordinateur portable")
    print("4) Box > Wi-Fi > Ordinateur portable")
    reponse = " "
    while reponse not in "1234": 
        reponse = input("\nRéponse à la situation n°2: ")
        if reponse in "1234":
            if reponse == "2":
                print("Bravo!")
                total += 1
            else:
                print("Dommage!")
        else: print("Réponse inexistante")
   
    print(f"Situation n°3: Vous écoutez le répondeur du téléphone sur l'ordinateur fixe\n{75*'-'}")
    print("1) Téléphone > Câble RJ11 > Box > Wi-Fi > Ordinateur fixe")
    print("2) Internet > Box > Câble RJ45 > Ordinateur fixe")
    print("3) Téléphone > Câble RJ11 > Box > CPL > réseau élec. > CPL > Câble RJ45 > Téléviseur+Boîtier")
    print("4) Téléphone > Câble RJ11 > Box > Câble RJ45 > Ordinateur fixe")
    reponse = " "
    while reponse not in "1234": 
        reponse = input("\nRéponse à la situation n°3: ")
        if reponse in "1234":
            if reponse == "4":
                print("Bravo!")
                total += 1
            else:
                print("Dommage!")
        else: print("Réponse inexistante")
    
    print(f"\nTotal: {total}/3")
    
## adresses ip
def mise_en_forme(octet):
        binaire = str(bin(octet))[2:].zfill(8)
        return binaire[:4]+" "+binaire[4:]
        
def nettoyage_bin(saisie):
    temp = ""
    for c in saisie:
        if c in "01./":
            temp += c
    return temp
    
def nettoyage_dec(saisie):
    temp = ""
    for c in saisie:
        if c in "0123456789./":
            temp += c
    return temp
        
def activite2_ex1():
    # conv dec > bin
    from random import randint
    boucle = True
    while boucle:
        oct1, oct2, oct3, oct4 = randint(12,222),randint(128,198),randint(24,98),randint(1,48)
        add_dec = f"{oct1}.{oct2}.{oct3}.{oct4}"
        reponse = mise_en_forme(oct1)+"."+mise_en_forme(oct2)+"."+mise_en_forme(oct3)+"."+mise_en_forme(oct4)
        proposition = nettoyage_bin(input(f"Convertir {add_dec}: "))
        
        octets = proposition.split('.')
        add = ""
        for o in octets:
            add += str(int("0b"+o,2))+"."
        
        if not add[:-1] == add_dec:
            print("Dommage, c'était: ", reponse,"\n")
        else:
            print("Bravo!\n")
        boucle = input("Appuyer sur Entrée pour recommencer (taper non pour arrêter): ") == ""
        add_dec = ""
        
def activite2_ex2():
    # conv bin > dec
    from random import randint
    boucle = True
    while boucle:
        oct1, oct2, oct3, oct4 = randint(12,222),randint(128,198),randint(24,98),randint(1,48)
        add_dec = f"{oct1}.{oct2}.{oct3}.{oct4}"
        reponse = mise_en_forme(oct1)+"."+mise_en_forme(oct2)+"."+mise_en_forme(oct3)+"."+mise_en_forme(oct4)
        proposition = nettoyage_dec(input(f"Convertir {reponse}: "))
        
        if not proposition == add_dec:
            print("Dommage, c'était: ", add_dec,"\n")
        else:
            print("Bravo!\n")
        boucle = input("Appuyer sur Entrée pour recommencer (taper non pour arrêter): ") == ""
        add_dec = ""
  
def activite2_ex3(add_dec = ""):
    # adresses réseau / machine 
    from random import randint
    if add_dec == "":
        oct1, oct2, oct3, oct4,masq = randint(12,222),randint(128,198),randint(24,98),randint(1,48),randint(20,27)
        add_dec = f"{oct1}.{oct2}.{oct3}.{oct4}/{masq}"
    else:
        liste = add_dec.split('.')
        temp = liste[3].split("/")
        liste.pop(3)
        liste += temp
        oct1, oct2, oct3, oct4,masq = int(liste[0]),int(liste[1]),int(liste[2]),int(liste[3]),int(liste[4])
    print("Donnée",add_dec)
    octets = [bin(oct1)[2:].zfill(8), bin(oct2)[2:].zfill(8),bin(oct3)[2:].zfill(8),bin(oct4)[2:].zfill(8)]
    add_res = ""
    for o in octets:
        add_res += o
    
    add_res2 = add_res[:masq]
    add_mach = "0" * (len(add_res2)) + add_res[masq:]
    while len(add_res2) < 32:
        add_res2 += '0'
    
    dict = {}
    dict["Reseau"] = str(int(add_res2[:8],2)) + "." + str(int(add_res2[8:16],2)) + "." + str(int(add_res2[16:24],2)) + "." + str(int(add_res2[24:],2))
    dict["Machine"] = str(int(add_mach[:8],2)) + "." + str(int(add_mach[8:16],2)) + "." + str(int(add_mach[16:24],2)) + "." + str(int(add_mach[24:],2))
    for cle in dict:
        test = dict[cle] == input(f'\nProposition pour adresse {cle}: ')
        if not test:
            print(dict[cle])
        else:
            print("Bravo!")
        
def activite2_ex4(add_dec = ""):
    # adresses caracteristiques  
    from random import randint
    if add_dec == "":
        oct1, oct2, oct3, oct4,masq = randint(12,222),randint(128,198),randint(24,98),randint(1,48),randint(20,27)
        add_dec = f"{oct1}.{oct2}.{oct3}.{oct4}/{masq}"
    else:
        liste = add_dec.split('.')
        temp = liste[3].split("/")
        liste.pop(3)
        liste += temp
        oct1, oct2, oct3, oct4,masq = int(liste[0]),int(liste[1]),int(liste[2]),int(liste[3]),int(liste[4])
    print("Donnée",add_dec)
    octets = [bin(oct1)[2:].zfill(8), bin(oct2)[2:].zfill(8),bin(oct3)[2:].zfill(8),bin(oct4)[2:].zfill(8)]
    add_res = ""
    for o in octets:
        add_res += o
    
    add_res = add_res[:masq]
    add_broad = add_res[:masq]
    add_prem = add_res[:masq]
    add_dern = add_res[:masq]
    add_masq = "1"*masq + "0"*(32 - masq)
    while len(add_res) < 31:
        add_res += '0'
        add_prem += '0'
        add_dern += '1'
        add_broad += '1'
    add_res += '0'
    add_prem += '1'
    add_dern += '0'
    add_broad += '1'
   
    dict = {}
    dict["Reseau"] = str(int(add_res[:8],2)) + "." + str(int(add_res[8:16],2)) + "." + str(int(add_res[16:24],2)) + "." + str(int(add_res[24:],2))
    dict["Premiere"] = str(int(add_prem[:8],2)) + "." + str(int(add_prem[8:16],2)) + "." + str(int(add_prem[16:24],2)) + "." + str(int(add_prem[24:],2))
    dict["Dernière"] = str(int(add_dern[:8],2)) + "." + str(int(add_dern[8:16],2)) + "." + str(int(add_dern[16:24],2)) + "." + str(int(add_dern[24:],2))
    dict["Broadcast"] = str(int(add_broad[:8],2)) + "." + str(int(add_broad[8:16],2)) + "." + str(int(add_broad[16:24],2)) + "." + str(int(add_broad[24:],2))
    dict["Masque"] = str(int(add_masq[:8],2)) + "." + str(int(add_masq[8:16],2)) + "." + str(int(add_masq[16:24],2)) + "." + str(int(add_masq[24:],2))
    for cle in dict:
        test = dict[cle] == input(f'\nProposition pour adresse {cle}: ')
        if not test:
            print(dict[cle])
        else:
            print("Bravo!")
    
