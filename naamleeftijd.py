def naamleeftijdFunction():
    naam = input("Wat is uw naam? (type stop om te stoppen)")
    if naam == "stop":
        quit()
    else:
        leeftijd = input("En uw leeftijd? (type stop om te stoppen)")
        if leeftijd == "stop":
            quit
        else:
            print("Hallo",naam+", uw leeftijd is",leeftijd,"jaar")
            naamleeftijdFunction()


naamleeftijdFunction()