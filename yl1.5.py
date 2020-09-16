def trahv():
    nimi = str(input("Palun sisestage oma nimi: "))
    lubatud_kiirus = int(input("Palun sisestage lubatud kiirus: "))
    tegelik_kiirus = int(input("Palun sisestage tegelik kiirus: "))
    vastus = (tegelik_kiirus - lubatud_kiirus)*3
    if vastus > 190:
        vastus = 190
        print(nimi + ", teie trahv on " + str(vastus) + " eurot.")
    else:
        print(nimi + ", teie trahv on " + str(vastus) + " eurot.")

trahv()

