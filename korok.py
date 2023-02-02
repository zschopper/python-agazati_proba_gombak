'''2. feladat:    összesen 14p szerezhető, a modul neve: korok.py
minta:
II/A, B, C:
           	20 : 34 : 78 : 83 : 90
II/D, E:
           	Első idős ember korának helye a listában: 2.



A.	Kérj be 5 egész számot a felhasználótól, melyek az egyes személyek korát jelentik! [0,120] (4p)
B.	A bekért  értékeket tárolja lista adatszerkezetben! (1p)
C.	Írasd ki a képernyőre a számokat : -tal (kettősponttal) elválasztva. A : jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.	Írj függvényt elso_idos néven, ami megkeresi az első  70 év feletti kort. A visszatérési érték legyen egy egész szám, melynek a kornak az INDEX-ét tartalmazza, a függvény bemenete a lista! (3p)
E.	Az elso_idos függvény eredményét írasd ki a mintának megfelelően a konzolra, amit konzolra_ir nevű metódusban fogalmazz meg! (2p)
F.	Az elso_idos függvény eredményét írasd ki a mintának megfelelően a oreg.txt nevű fájlba, amit fajl_ir nevű metódusban fogalmazzon meg! (2p)

'''

class Korok:

    def beker(self):

        # return [20, 34, 78, 83, 90]

        lista = []
        while len(lista) < 5:
            szam = int(input("Adjon meg egy számot: "))
            if 0 <= szam <= 120:
                lista.append(szam)
            else:
                print("A megadott kornak 0 és 120 között kell legyen! ")
        return lista

    def osszefuz(self, lista):
        elvalaszto = ":"
        szoveg = ""
        if lista:
            szoveg = str(lista[0])
            i = 1
            while i < len(lista):
                szoveg += elvalaszto + str(lista[i])
                i += 1
        return szoveg

    def elso_idos(self, lista):
        i = 0
        while i < len(lista) and lista[i] < 70:
            i += 1

        if i < len(lista):
            return i
        else:
            return -1

    def konzolra_ir(self, lista):
        idx = self.elso_idos(lista)
        print(f"Első idős ember korának helye a listában: {idx}.")

    def fajl_ir(self, lista, fajlnev):
        idx = self.elso_idos(lista)
        fh = open(fajlnev, "w", encoding="utf-8")
        fh.write(f"Első idős ember korának helye a listában: {idx}.")
        fh.close()
