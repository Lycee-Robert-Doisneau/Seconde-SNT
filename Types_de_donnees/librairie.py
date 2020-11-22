#!/usr/bin/python
# -*- coding: utf-8 -*-

# ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
# ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
#     ╒ ╕ ╘ ╛ ╞ ╡ ╤ ╧ ╪
#     ╓ ╖ ╙ ╜ ╟ ╢ ╥ ╨ ╫

## conversion binaire > décimal  
def activite1_ex1():
    from random import randint
    boucle = True
    total, bon = 0, 0
    while boucle:
        total += 1
        nombre = randint(0,256)
        binaire = str(bin(nombre))[2:].zfill(8)
        binaire = binaire[:4]+" "+binaire[4:]
        if bin(int(input(f"Ex.{total} Proposition pour {binaire}: "))) == bin(nombre):
            bon += 1
            print("bravo!",str(round(bon/total*100)),"%\n")
        else: 
            print("dommage... à retenter!",str(round(bon/total*100)),"%\n")
        
        boucle = input("Appuyer sur entrée pour continuer (taper stop pour arrêter)") == ""
    print('-'*15)
    print("résultat final:",str(round(bon/total*100)),"%")    
  
## conversion décimal > binaire    
def activite1_ex2():
    from random import randint
    boucle = True
    total, bon = 0, 0
    while boucle:
        total += 1
        nombre = randint(0,256)
        if bin(int(str(input(f"Ex.{total} Proposition pour {nombre}: ")),2)) == bin(nombre):
            bon += 1
            print("bravo!",str(round(bon/total*100)),"%\n")
        else: 
            print("dommage... à retenter!",str(round(bon/total*100)),"%\n")
        
        boucle = input("Appuyer sur entrée pour continuer (taper stop pour arrêter)") == ""
    print('-'*15)
    print("résultat final:",str(round(bon/total*100)),"%")
    
## hexa > ascii
def activite2_ex1():
    total = 1
    essai = 'essai !!!'
    boucle = input(f"proposition n°{total}: ") != chr((0x41))+chr((0x53))+chr((0x43))+chr((0x49))+chr((0x49))
    while boucle:
        total += 1
        essai = 'essais'
        print("dommage... à retenter!")
        boucle = input(f"proposition n°{total}: ") != chr((0x41))+chr((0x53))+chr((0x43))+chr((0x49))+chr((0x49))
    print(f"Bravo! En {total} {essai}")    
        
## binaire > ascii
def activite2_ex2():
    total = 1
    essai = 'essai !!!'
    boucle = input(f"proposition n°{total}: ") != chr((0b1010011))+chr((0b101110))+chr((0b1001110))+chr((0b101110))+chr((0b1010100))+chr((0b101110))
    while boucle:
        total += 1
        essai = 'essais'
        print("dommage... à retenter!")
        boucle = input(f"proposition n°{total}: ") != chr((0b1010011))+chr((0b101110))+chr((0b1001110))+chr((0b101110))+chr((0b1010100))+chr((0b101110))
    print(f"Bravo! En {total} {essai}")    
        
## décimal > ascii
def activite2_ex3():
    total = 1
    essai = 'essai !!!'
    boucle = input(f"proposition n°{total}: ") != chr((99)) + chr((104)) + chr((114)) + chr((40)) + chr((57)) + chr((48)) + chr((41)) + chr((61)) + chr((39)) + chr((90)) + chr((39))
    while boucle:
        total += 1
        essai = 'essais'
        print("dommage... à retenter!")
        boucle = input(f"proposition n°{total}: ") != chr((99)) + chr((104)) + chr((114)) + chr((40)) + chr((57)) + chr((48)) + chr((41)) + chr((61)) + chr((39)) + chr((90)) + chr((39))
    print(f"Bravo! En {total} {essai}")    
        
## cryptographie
def crypter_une_lettre(lettre_claire, cle):
    temp = ord(lettre_claire)
    if temp >= 97 and temp <= 122:
        lettre_cryptee = chr((temp - 97 + cle) % 26 + 97)
    elif temp >= 65 and temp <= 90:
        lettre_cryptee = chr((temp - 65 + cle) % 26 + 65)
    else:
        lettre_cryptee = lettre_claire
    return lettre_cryptee
 
def crypter_un_texte(texte_clair, cle):
    texte_crypte = ''
    for lettre_claire in texte_clair:
        texte_crypte += crypter_une_lettre(lettre_claire,cle)
    return texte_crypte
    
def activite4_ex1(): 
    from random import randint
    cle = randint(-5,10)
    total = 1
    essai = 'essai !!!'
    boucle = input(f"Crypter 'cesar' avec une clé de {cle} proposition n°{total}: ") != crypter_un_texte('cesar',cle)
    while boucle:
        total += 1
        essai = 'essais'
        print("dommage... à retenter!")
        boucle = input(f"Crypter 'cesar' avec une clé de {cle} proposition n°{total}: ") != crypter_un_texte('cesar',cle)
    print(f"Bravo! En {total} {essai}")