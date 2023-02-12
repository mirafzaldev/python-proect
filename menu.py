import os
import register

def menu():
    print('''
Assalomalekum xurmatli mijon xush kelibsiz 
bizning menu blan tanishing
        ''')
    summa = []
    menu = {
        "qozon kabob"     : 30_000,
        "shashlik donasi" : 12_000,
        "shorva"          : 21_000,
        "manti"           : 4000,
        "osh 1 porsiya"   :  30_000,
        "chuchvara"       : 24_000
    }
    salatlar = {
        "achichiq chuchuq" : 8000,
        "fransuzki"        : 10000,
        "mujskoi_kapriz"   : 10000
    }
    ichimlik = {
        "choy qora kok": 2000,
        "cola 0.5"     :  6000,
        "cola 1"       : 11000,
        "cola 1.5"     : 15000,
        "limon choy"   : 5000,
        "coffee"       : 5000
    }
    disert = {
        "muz_qaymoq"       : 11000,
        "tort shokoladni " : 15000,
        "pirojni"          : 8000,
        "tort qaymoqli"    : 15000
    }
    for x , y in menu.items():
        print(f'''{x} : {y}''')
    birinchsi = input("Birichsiaga nma buyurasiz: ")
    os.system('cls')
    if birinchsi in  menu.keys():
        summa.append(menu[birinchsi])
    else:
        print("menu da yoq narsani tanladingiz!")
    os.system('cls')
    print("salatlarimz blan tanishing!")
    for x , y in salatlar.items():
        print(f''' {x} : {y}''')
    salat = input("Salat qoshamizmi : ")
    if salat in salatlar.keys():
        summa.append(salatlar[salat])
    else:
        print("menu da yoq narsani tanladingiz")
    os.system('cls')
    print("ichimliklarimiz!")
    for x , y in ichimlik.items():
        print(f'''{x} : {y} ''')
    ichish_uchun = input("ichishga nma buyurasiz: ")
    if ichish_uchun in ichimlik.keys():
        summa.append(ichimlik[ichish_uchun])
    else: 
        print("bunday buyurtma menu da yoq")
    os.system('cls')
    print("Disertlarimiz!")
    for x , y in disert.items():
        print(f'''{x} : {y}''')
    disertga = input("disertga nma buyrasiz: ")
    if disertga in disert.keys():
        summa.append(disert[disertga])
    roixat = open("roixat.txt" , "a")
    os.system('cls')
    print(f'''
    umummi xisobda sizdan : {sum(summa)} so'm boldi 
    itlmos tolovni amalga oshiring buyurtmangiz tez orada tayor boladi!
           😊''')
    roixat.write(f'''
    ismi: {register.name}
    telefon raqami: {register.tel}
    birichsiga: {birinchsi}
    salat: {salat}
    ichishmilk : {ichish_uchun}
    diser: {disertga}
    ummumi xisobda: {sum(summa)} so'm tolandi
            ''')
