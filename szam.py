'''
I/A:
A generált szám: 45

I/B:
A szám öttel és hárommal is osztható!

A.	Generálj egy véletlen egész  számot az [1, 50] zárt intervallumban!  (2p)
B.	A program írja ki a következők egyikét: (a mintának megfelelően - 1p):
•	Amennyiben a szám 5-tel osztható:
“A szám öttel osztható!”,
•	Amennyiben a szám 3-mal osztható:
“A szám hárommal  osztható!”,
•	Amennyiben a szám 5-tel és 3-mal is osztható:
“A szám öttel és hárommal is osztható!”,

'''
import random

class Szam:

    def __init__(self) -> None:
        self.szam = int(random.random() * 51 + 1)

    def oszthato(self):
        if self.szam % 5 == 0 and self.szam % 3 == 0:
            return "A szám öttel és hárommal is osztható!"
        elif self.szam % 5 == 0:
            return "A szám öttel osztható!"
        elif self.szam % 3 == 0:
            return "A szám hárommal osztható!"
        else:
            return ""
