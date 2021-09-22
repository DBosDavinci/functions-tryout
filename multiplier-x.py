getal = int(input("Van welk getal wilt u de tafel zien?"))

def tafelFunction(a: int):
    for x in range(1,11):
        total = a * x
        print(total)
        x=+1

tafelFunction(getal)