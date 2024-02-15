

#luodaan tiedosto mihin tallennetaan
import time
while True:
    print("(1) Lue muistikirjaa")
    print("(2) Lisää merkintä")
    print("(3) Tyhjennä muistikirja")
    print("(4) Lopeta")
    valinta = int(input("Mitä haluat tehdä?: "))
    if valinta == 1:
        kahva = open("muistio.txt", "r")
        teksti = kahva.read()
        print(teksti)
        kahva.close()
    elif valinta == 2:
        tiedosto = open("muistio.txt", "a")
        lisays = input("kirjoita uusi merkintä: ")
        tiedosto.write("\n")
        aika = time.strftime("%X %x")
        tiedosto.write(lisays+":::"+aika)
        tiedosto.close()
    elif valinta == 3:
        tiedosto = open("muistio.txt", "w")
        tiedosto.close()
        print("Muistio tyhjennetty.")
    elif valinta == 4:
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")