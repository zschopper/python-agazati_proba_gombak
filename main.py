from szam import Szam
from korok import Korok
from gombak import Gombak

sz = Szam()

print(f"I/A:\n\tA generált szám: {sz.szam}")


oszth = sz.oszthato()

if oszth:
    print(f"I/B:\n\t{oszth}")
else:
    print("I/B:\n")

print()

k = Korok()

lista = []
k.beker(lista)

print(f"II/A, B, C:\n\t {k.osszefuz(lista)}")

print("II/D, E:\n\t", end="")
k.konzolra_ir(lista)
k.fajl_ir(lista, "oreg.txt")

g = Gombak("gombak.txt")
db = g.gombak_szama()
print(f"III/A, B:\n\tA gombák száma: {db}.")

pap = g.papsapka()
print(f"III/C:\n\tAz első papsapkagomba neve: {pap.nev}")

tin = g.tinoru()
print(f"III/D:\n\tA tinóru gombák száma: {tin}")
