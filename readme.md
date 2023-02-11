
# Ágazati vizsga gyakorló  Python - 2023

A feladatokat külön modulokban oldja meg, a modulok nevei a feladatokban találhatók!
A főprogramból (main.py) hívja meg az egyes modulok metódusait a feladatban meghatározott neveikkel (1p)!
A projektet agazati_2023_a néven mentse, majd a munkáját sajat_nev.zip (Pl.: Nagy_Virag.zip) nevű állományban adja le! (1p)

## 1. feladat

Összesen 7p szerezhető, a modul neve: **szam.py**

minta:  
(a stílus kialakítása nem feladat, de a feladat sorszámának és betűjelének a kiíratása igen):

```
I/A:
    A generált szám: 45

I/B:
    A szám öttel és hárommal is osztható!
```

A. Generálj egy véletlen egész  számot az [1, 50] zárt intervallumban!  (2p)  
B. A program írja ki a következők egyikét: (a mintának megfelelően – 1p):  
    • Amennyiben a szám 5-tel osztható:  
      “A szám öttel osztható!”,  
    • Amennyiben a szám 3-mal osztható:  
      “A szám hárommal  osztható!”,  
    • Amennyiben a szám 5-tel és 3 – mal is osztható:  
      “A szám öttel és hárommal is osztható!”  

A három kiírás közül csak az egyik jelenjen meg a képernyőn!. (4p + 1p) 

## 2. feladat

Összesen 14p szerezhető, a modul neve: **korok.py**

minta:

```
II/A, B, C:
    20 : 34 : 78 : 83 : 90

II/D, E:
    Első idős ember korának helye a listában: 2.
```

kimutatas.txt tartalma:

```
II/F:
    Első idős ember korának helye a listában: 2.
```

A. Kérj be 5 egész számot a felhasználótól, melyek az egyes személyek korát jelentik! [0,120] (4p)  
B. A bekért  értékeket tárolja lista adatszerkezetben! (1p)  
C. Írasd ki a képernyőre a számokat : -tal (kettősponttal) elválasztva. A : jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)  
D. Írj függvényt elso_idos néven, ami megkeresi az első  70 év feletti kort. A visszatérési érték legyen egy egész szám, melynek a kornak az INDEX-ét tartalmazza, a függvény bemenete a lista! (3p)  
E. Az elso_idos függvény eredményét írasd ki a mintának megfelelően a konzolra, amit konzolra_ir nevű metódusban fogalmazz meg! (2p)  
F. Az elso_idos függvény eredményét írasd ki a mintának megfelelően a oreg.txt nevű fájlba, amit fajl_ir nevű metódusban fogalmazzon meg! (2p)  

## 3. feladat

Összesen 17p szerezhető, a modul neve: **gombak.py**

A gombak.txt forrásállomány, gombák adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A gep.txt állomány szerkezete:

* gomba neve: pl.: piros csészegomba
* nemzettség pl.: csészegomba
* évszak pl.: tél, tavasz

Az állomány első sora a mezőneveket tartalmazza @  jellel elválasztva.
A megoldás mintája:

```
III/A, B:
    A gombák száma: 78.
III/C:
    Az első papsapkagomba neve: homoki papsapka.
III/D:
    A tinóru gombák száma: 14.
```

A. Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a gombák.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)  
B. Írassa ki a gombák számát a mintának megfelelően a konzolra! A metódus neve legyen gombak_szama! (2p)  
C. Határozza meg és írassa ki a konzolra a minta szerint, hogy a melyik a papsapkagombák nemzettségben melyik az első gomba, amelyik szerepel a listában?  A metódus neve legyen papsapka! (4p)  
D. Írassa ki konzolra a mintának megfelelően a tinóru nemzettséghez tartozó gombák számát! A metódus neve tinoru legyen (4p)  
