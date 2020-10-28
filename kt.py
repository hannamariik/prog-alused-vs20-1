import random

hind = float(input("Sisestage kõneminuti hind: "))
koned = int(input("Sisestage kõnede arv: "))

#Loon listi kuhu panen for tsükli ja randinti abil kõnekestused
konekestused = []
for i in range (koned):
    konekestused.append(random.randint(1, 1000))

#Loon muutuja arve, kuhu hakkan juurde liitma iga kõne hinda
#Kasutan for tsüklit, et kõnekestuste list üks haaval läbi käia.
#Kasutan if tsüklit, et eraldada kõned, mille pikkus on kuni 60 sekundut või üle 600 sekundi.

def kone_maksumus(konekestused, hind):
    arve = 0
    for j in konekestused:
        if j <= 60:
            print("kõne maksumus: " + str(hind))
            arve += hind
        elif j >= 600:
             print("kõne maksumus: " + str(hind * 10))
             arve += hind * 10
        else:
            print("kõne maksumus: " + str(hind * (j/60)))
            arve += (hind * (j/60))
    print("Kogu arve: " + str(round(arve, 2))+ "EUR")

kone_maksumus(konekestused, hind)    