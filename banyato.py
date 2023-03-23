"""
1. feladat
Olvassa be és tárolja el a melyseg.txt állomány adatait, és annak felhasználásával oldja
meg a következő feladatokat! 
"""
print("1.Feladat")
melysegek=[]

with open("melyseg.txt","r",encoding="UTF-8") as fm1:
    fm1.readline()
    fm1.readline()
    for sor in fm1:
        seged_lista=list(map(int,sor.strip().split()))
        melysegek.append(seged_lista)

from colorama import Fore, Back

for melyseg_sor in melysegek:
    for melyseg in melyseg_sor:
        if melyseg>0:
            print(f"{Back.BLUE}{Fore.WHITE}{melyseg:2d}", end=" ")
        else:
            print(f"{Back.RESET}{Fore.RESET}{melyseg:2d}", end=" ")
        

    print()

"""
2. feladat
Kérje be egy mérési eredmény sor- és oszlopazonosítóját, majd írassa ki az adott helyen
mért adatot a képernyőre! (A sorok és oszlopok számozása kezdődjön 1-gyel!) 
2. feladat
A mérés sorának azonosítója=12
A mérés oszlopának azonosítója=6
A mért mélység az adott helyen 33 dm
"""
print("2.feladat")
be_sor=int(input("A mérés sorának azonosítója:") or "12")
be_oszlop=int(input("A mérés oszlopának azonosítója:")or 6)
print(f"A mérés oszlopának azonosítója:{melysegek[be_sor-1][be_oszlop-1]}dm")


"""
3. feladat
Határozza meg a tó (vagyis az ábrán szürkével jelölt rész) felszínének területét, valamint
a tó átlagos mélységét! Írassa ki a két eredményt a mintának megfelelően a képernyőre!
A tó átlagos mélysége méterben kifejezve, két tizedesjegy pontossággal jelenjen meg! 
3. feladat
A tó felszíne: 646 m2, átlagos mélysége: 4,28 m
"""

def megszamolas(m):
    db=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                db+=1
    return db
atlagos_melyseg=0

def atlagolas(m):
    osszeg=0
    darab=0
    for seged_lista in m:
        for elem in  seged_lista:
            if elem>0:
                darab+=1
                osszeg+=elem
    return osszeg/darab
print("3.Feladat")
print(f"A tó felszíne: {megszamolas(melysegek)} m2, átlagos mélysége: {atlagolas(melysegek)/10:0.2f} m")

"""
4. feladat
Mekkora a tó legnagyobb mélysége, és hol a legmélyebb a tó? Jelenítse meg a választ
a képernyőn! A legmélyebb pont koordinátáit a mintának megfelelően (sor; oszlop)
formában írassa ki! Ha több ilyen mérési eredmény is van, mindegyik koordinátapárja
jelenjen meg!
4. feladat
A tó legnagyobb mélysége: 98 dm
A legmélyebb helyek sor-oszlop koordinátái:
(14; 20) (26; 11) (32; 16)
"""
print("4.Feladat")
def max_kivalasztas(m):
    max_sor=0
    max_oszlop=0
    for i in range(1,len(m)):
        for j in range(len(m[i])):
         if m[max_sor][max_oszlop]<m[i][j]:
             max_sor=i
             max_oszlop=j
    return max_sor, max_oszlop
max_kivalasztas(melysegek)
max_s, max_o=max_kivalasztas(melysegek)
print(f"A tó legnagyobb mélysége: {max_kivalasztas(melysegek)} dm")

print(f"A legmélyebb helyek sor-oszlop koordinátái:")
def legmelyebb_pontok_koordinatai(m,max):
    for sor_index,sor in enumerate(m):
        for oszlop_index, elem in enumerate(sor):
            if elem==max:
                print(f"({sor_index+1};{oszlop_index+1})",end="")


legmelyebb_pontok_koordinatai(melysegek,melysegek[max_s][max_o])
#legmelyebb_pontok_koordinatai(melysegek, melysegek[max_sor][max_oszlop])    
#(14; 20) (26; 11) (32; 16)