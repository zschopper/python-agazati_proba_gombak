'''
A gombak.txt forrásállomány, gombák adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A gep.txt állomány szerkezete:
·         gomba neve: pl.: piros csészegomba
·         nemzettség pl.: csészegomba
·         évszak pl.: tél, tavasz
Az állomány első sora a mezőneveket tartalmazza @  jellel elválasztva.
A megoldás mintája:
III/A, B:
         A gombák száma: 78.
III/C:
         Az első papsapkagomba neve: homoki papsapka.
III/D:
         A tinóru gombák száma: 14.
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a gombák.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki a gombák számát a mintának megfelelően a konzolra! A metódus neve legyen gombak_szama! (2p)
C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy a melyik a papsapkagombák nemzettségben melyik az első gomba, amelyik szerepel a listában?  A metódus neve legyen papsapka! (4p)
D.	Írassa ki konzolra a mintának megfelelően a tinóru nemzettséghez tartozó gombák számát! A metódus neve tinoru legyen  (4p)

'''
class Gomba:

    def __init__(self, lista) -> None:
        if len(lista) == 3:
            self.nev, self.nemzettseg, self.evszak = lista
        else:
            raise Exception("Hibás értékek!")

        def __str__(self):
            return f"{self.nev} {self.nemzettseg} {self.evszak}"


class Gombak:
    def __init__(self, fajlnev) -> None:
        self.lista = []

        fh = open(fajlnev, "r", encoding="utf-8")
        sorok = fh.read().split("\n")
        fh.close()
        i = 1
        while i < len(sorok):
            adat = sorok[i].split("@")
            self.lista.append(Gomba(adat))
            i += 1

    def gombak_szama(self):
        return len(self.lista)

    def papsapka(self):
        i = 0
        while i < len(self.lista):
            if (self.lista[i].nemzettseg.rstrip() == "papsapkagombák"):
                return self.lista[i]
            i += 1

    def tinoru(self):
        i = 0
        db = 0
        while i < len(self.lista):
            if (self.lista[i].nemzettseg.rstrip() == "tinóru"):
                db += 1
            i += 1
        return db

