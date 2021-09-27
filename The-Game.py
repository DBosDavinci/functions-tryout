# The Game

A = ["a", "A"]
B = ["b", "B"]

name = input("Welcome to The Game Zombie apocalypse, please choose your name!\n>")
print("\nThe objective of this game is to reach the airport, which is close to the forest outside of the city. Once you get there you can escape from the zombie infected city.\n")

energy = 50
print("This game also includes an energy system, so make sure your energy will be above 0.")
print("You start with",energy,"energy")
currentenergy = "Your current energy is:"

def energyTotal():
    print(currentenergy, energy)

keuze1 = input("\nYou wake up in an empty factory and hear some growling. You around and sees a zombie at the entrance of the factory. What will you do?\n"
"a) Run for it\n"
"b) Look for a weapon to slaughter it\n>")

if keuze1 in A:
    energy = energy - 20
    energyTotal()
    keuze2 = input("You chose to run for it. You walk outside and see a forest close by and a hospital on the opposite side of the road. Where will you go?\n"
    "a) Go to the nearby forest\n"
    "b) Go to the hospital on the opposite side of road\n>")
    if keuze2 in A:
        energy = energy - 5
        energyTotal()
        keuze3 = input("You arrive in the forest, you arrive at an abandoned house. Will you go inside or go further into the forest?\n"
        "a) Enter the abandoned house\n"
        "b) Go deeper into the forest?\n>")
        if keuze3 in A:
            energy = energy - 5
            energyTotal()
            keuze4 = input("After entering the house, you spot an energy drink. Because you ran from the zombie in the beginning you feel quite tired, will you drink the energy drink?\n"
            "a) Drink the energy drink\n"
            "b) Don't drink the energy drink\n>")
            if keuze4 in A:
                energy = energy + 30
                energyTotal()
                keuze5 = input("In the house you encounter a zombie, will you attack it or run from it?\n"
                "a) Attack the zombie\n"
                "b) Run from the zombie\n>")
                if keuze5 in A and energy >= 50:
                    energy = energy - 20
                    energyTotal()
                    keuze6 = input("You succesfully killed the zombie, and you feel quite hungry after killing it. Will you eat its flesh?\n"
                    "a) Eat the zombie's flesh\n"
                    "b) Don't eat the zombie's flesh\n>")
                    if keuze6 in A:
                        energy = energy + 10
                        energyTotal()
                        keuze7 = input("After eating the zombie's flesh, you leave the house and go back on the forest's road. Will you go right or left?\n"
                        "a) Go left\n"
                        "b) Go right\n>")
                        if keuze7 in A:
                            print("You walk to the left, but you didn't read the sign that said Minefield. RIP")
                        elif keuze7 in B:
                            energy = energy - 10
                            energyTotal()
                            keuze8 = input("You go right and end up on a very long road, you walk an endless path and wonder if its worth staying on the road. What will you do?\n"
                            "a) Go back into the forest\n"
                            "b) Stay on the road\n>")
                            if keuze8 in A:
                                energy = energy - 5
                                energyTotal()
                                keuze9 = input("You go back into the forest. You spot a fence, but you are feeling quite tired. Will you go climb over it or look for some food.\n"
                                "a) Try to find a way around the fence\n"
                                "b) Try to climb over the fence\n>")
                                if keuze9 in A:
                                    print("You try to find a way around the fence, but instead of finding a way around it, you encounter a zombie and fail to kill it. RIP")
                                elif keuze9 in B:
                                    energy = energy - 10
                                    energyTotal()
                                    keuze10 = input("You climb over the fence, and you find out you ended up on the airport. You see a man standing at the entrance of the airport. Will you inform him of the zombie apocalypse or go directly to the airplane?\n"
                                    "a) Speak to the man\n"
                                    "b) Go straight to the airplane\n>")
                                    if keuze10 in A:
                                        print("You walk to the man on the airport, just before you can open your mouth to speak to him you notice he has a weird look on his face. The man walks straight towards you and you try"
                                        "to run from him, but there is already a swarm of zombies behind you. RIP")
                                    elif keuze10 in B:
                                        print("You walk to the airplane, you drive onto the flying path. A swarm of zombies is coming after you, but you are out of reach. You fly away and you completed the game! Congratulations",name,"!")
                            elif keuze8 in B and energy <= 40:
                                print("After walking another kilometer or so, you encounter a zombie on the road. You fight it and win, but later die of wounds and starvation. RIP")                   
                    elif keuze6 in B:
                        energy = energy - 5
                        energyTotal()
                        keuze7 = input("You decided not to eat the flesh from the zombie you just killed. When continuing walking back on the road, you can go two ways. Right or Left?\n"
                        "a) Go right\n"
                        "b) Go left\n>")
                        if keuze7 in A:
                            energy = energy - 10
                            energyTotal()
                            keuze8 = input("You go right and end up on a very long road, you walk an endless path and wonder if its worth staying on the road. What will you do?\n"
                            "a) Go back into the forest\n"
                            "b) Stay on the road\n>")
                            if keuze8 in A:
                                energy = energy - 5
                                energyTotal()
                                keuze9 = input("You go back into the forest. You spot a fence, but you are feeling quite tired. Will you go climb over it or look for some food.\n"
                                "a) Try to climb over the fence\n"
                                "b) Look for food\n>")
                                if keuze9 in A and energy <= 10:
                                    print("You couldn't make the jump over the barbed wire on the fence, because you didnt have enough energy left. RIP")
                                elif keuze9 in B and energy <= 10:
                                    print("You go back further into the forest to look for some food, because you're feeling low on energy. But you fail to find any, so you die of starvation. RIP")
                            elif keuze8 in B:
                                print("After walking another kilometer or so, you encounter a zombie on the road. You fight it and win, but later die of wounds and starvation. RIP")
                        elif keuze7 in B:
                            print("You walk to the left, but you didn't read the sign that said Minefield. RIP")
                elif keuze5 in A:
                    print("You try to run from the zombie, but trip on the doorstep. It eats you alive. RIP")
            elif keuze4 in B:
                energy = energy - 5
                energyTotal()
                keuze5 = input("In the house you encounter a zombie, will you attack it or run from it?\n"
                "a) Attack the zombie\n"
                "b) Run from the zombie\n>")
                if keuze5 in A and energy != 50:
                    print("You try to attack the zombie, but you fail to swing at the zombie because you don't have enough energy left. RIP")
                elif keuze5 in B and energy != 50:
                    print("You try to run from the zombie, but you don't have enough energy left. RIP")
        elif keuze3 in B:
            energy = energy - 5
            energyTotal()
            keuze4 = input("You go deeper into the forest and you spot a boar, because you're feeling hungry you want to kill it, but can you take a boar?\n"
            "a) Try to kill the boar\n"
            "b) Try looking for some other food\n>")
            if keuze4 in A:
                print("You try to kill the boar you found, but it rams your leg and you cant walk anymore, You can't move and later die of starvation. RIP")
            elif keuze4 in B:
                energy = energy - 5
                energyTotal()
                keuze5 = input("You try looking for some other food, because the boar seems to dangerous. After walking around for a bit you find a bush with berries in it, you don't have much knowledge about it but the berries seem poisonous. Will you eat them?\n"
                "a) Eat the poisonous-looking berries\n"
                "b) Don't eat them and look for something else\n>")
                if keuze5 in A:
                    print("You try eating the poisonous-looking berries, but you immediately throw up and later die of starvation. RIP")  
                elif keuze5 in B:
                    energy = energy - 5
                    energyTotal()
                    keuze6 = input("You decide not to eat the berries, even though you are really hungry. You walk around for a bit more, but suddenly you trigger a trap and fall almost 5 meters deep. What will you do?\n"
                    "a) Try to climb out of the trap\n"
                    "b) Try to dig a tunnel out of the trap\n>")
                    if keuze6 in A and energy <= 10:
                        print("You try to climb out of the trap, but after reaching halfway, you fall to your death because you didnt have enough energy left. RIP")
                    elif keuze6 in B and energy <= 10:
                        print("You try to dig a tunnel out of the trap, but after digging for a while you're totally exhausted and die of starvation, because you didn't have enough energy left. RIP")  
    elif keuze2 in B:
        energy = energy - 5
        energyTotal()
        keuze3 = input("You walk up to the hospital, but the front door is open. You also spot a broken window on the side of the building. How will you enter the building\n"
        "a) Enter through the front door\n"
        "b) Enter through the broken window\n>")
        if keuze3 in A:
            print("You enter through the front door, but you immediately get ambushed by 3 zombies. RIP")
        elif keuze3 in B:
            energy = energy - 15
            energyTotal()
            keuze4 = input("You climb through the broken window and cut yourself, it's totally dark inside but you can see something shiny lying on the ground. You pick it up, to inspect it and you find out it's a needle. You feel pretty tired, but is it a good idea to inject yourself?\n"
            "a) Inject yourself with the needle you found lying on the ground.\n"
            "b) Don't inject yourself with the needle you found lying on the ground.\n>")
            if keuze4 in A:
                energy = energy + 15
                energyTotal()
                keuze5 = input("After injecting yourself with the needle, you start to feel pretty sick and dizzy. It probably wasn't a good idea to inject yourself with a needle, but how are you going to fix this?\n"
                "a) Drink some water and wait it out\n"
                "b) Inject yourself with some other needles lying on the ground\n>")
                if keuze5 in A:
                    energy = energy - 10
                    energyTotal()
                    keuze6 = input("After drinking some water, you don't feel any better, but you decide to move on. on the streets you see some zombies, will you go further inside the hospital or will you kill the zombies for food?\n"
                    "a) Go further inside the hospital\n"
                    "b) Kill the zombies on the street\n>")
                    if keuze6 in A:
                        energy = energy - 10
                        energyTotal()
                        keuze7 = input("Going further inside the hospital, you hear a zombie behind you, what will you do\n"
                        "a) Try to kill the zombie\n"
                        "b) Try to run away\n>")
                        if keuze7 in A:
                            print("You try to kill the zombie, but fail because of the effect from the needle. RIP")
                        elif keuze7 in B:
                            print("You try to run from the zombie, but fail because of the effect from the needle. RIP")
                    elif keuze6 in B:
                        print("You try to kill the zombies, but fail. They outnumbered you. RIP")
                elif keuze5 in B:
                    print("You die from an overdose. RIP")
            elif keuze4 in B:
                energy = energy - 5
                energyTotal()
                keuze5 = input("You walk further into the hospital and you smell something horrible coming from a room a couple of meters away. Will you go check it out?\n"
                "a) Check out the room\n"
                "b) Don't check out the room\n>")
                if keuze5 in A:
                    print("You go to check out the room, after entering the room you find out the horrible smell is a dead body, and a zombie is standing on top of it. It immediately jumps to you, and due to the injury you sustained earlier, the zombie kills you. RIP")
                elif keuze5 in B:
                    energy = energy - 5
                    energyTotal()
                    keuze6 = input("You don't go to check out the room, but you are feeling really low on energy, because of the injury you sustained earlier. You want to look for some food, but where?\n"
                    "a) Search the bin you saw before entering the hospital\n"
                    "b) Try to kill zombies on the streets\n>")
                    if keuze6 in A:
                        energy = energy - 5
                        energyTotal()
                        keuze7 = input("You went to go and check out the bin outside the hospital, in there you found some food, but it seems rotten. Will you eat it?\n"
                        "a) Eat the food\n"
                        "b) Don't eat the food\n>")
                        if keuze7 in A:
                            print("You decided not to eat the food you found, and walk along the steet looking for other food. You encounter a zombie, but due to your lack of energy you can't get away or kill the zombie. RIP")
                        elif keuze7 in B:
                            print("You eat the food and you immediately taste that it's very bad, but you keep eating because otherwise you will die of starvation. After finishing the food you feel really sick, and after a couple of minutes die. RIP")
                    elif keuze6 in B:
                        print("You go on the steets to kill some zombies to eat, but due to the injury you sustained earlier, you lack the ability to kill a zombie. RIP")
elif keuze1 in B:
    energy = energy - 5
    energyTotal()
    keuze2 = input("You find a broken glass bottle on the floor, you can use to try to kill the zombie. Will you try it?\n"
    "a) Attack the zombie\n"
    "b) Look for more weapons outside\n>")
    if keuze2 in A:
        print(name,"tries to kill the zombie, you succeed, but while you were killing it 5 other zombies entered the building. RIP")
    elif keuze2 in B:
        energy = energy - 5
        energyTotal()
        keuze3 = input("You decided to go look for more weapons, which way do you go?\n"
        "a) Go right\n"
        "b) Go left\n>")
        if keuze3 in A:
            energy = energy - 5
            energyTotal()
            keuze4 = input("You decided to walk to the left. When walking across the streets you spot an abandoned car and a house. Where will you go?\n"
            "a) Enter the house\n"
            "b) Try to break into the abandoned car\n>")
            if keuze4 in A:
                energy = energy - 5
                energyTotal()
                keuze5 = input("After entering the house, You can go into the living room or upstairs, where will you go?\n"
                "a) Go upstairs\n"
                "b) Go into the living room\n>")
                if keuze5 in A:
                    print(name,"decides to walk up the stairs, when you are about halfway upstairs a zombie comes around the corner. You startle and fall down the stairs and break your neck. RIP")
                elif keuze5 in B:
                    energy = energy - 5
                    energyTotal()
                    keuze6 = input("You go into the living room, there seems to be a curious smell. You want to figure out what it is.\n"
                    "a) Check the table\n"
                    "b) Check the closet\n>")
                    if keuze6 in A:
                        energy = energy - 5
                        energyTotal()
                        keuze7 = input("You check out the table, but you cant there seem te be anything. You go to further check out the house. Where do you go?\n"
                        "a) Go into the basement\n"
                        "b) Go into the kitchen\n>")
                        if keuze7 in A:
                            energy = energy - 5
                            energyTotal()
                            keuze8 = input("After going into the basement, you hear some loud growling. Will you check it out or run back up?\n"
                            "a) Check out the basement further\n"
                            "b) Run back upstairs\n>")
                            if keuze8 in A:
                                print("You walk further into the basement, even though you hear a lot of growling. You walk up to the boiler, and a zombie appears from behind it. Because you are low on energy you cant get away and the zombie eats you. RIP")
                            elif keuze8 in B:
                                energy = energy - 5
                                energyTotal()
                                keuze9 = input("You run back upstairs, but you trip on the stairs. The zombies catch up to you. What will you do?\n"
                                "a) Try to run from the zombies\n"
                                "b) Try to kill the zombies\n>")
                                if keuze9 in A and energy < 20:
                                    print("You try to run from the zombies, but because you are low on energy you can't get away. RIP")
                                elif keuze9 in B and energy < 20:
                                    print("You decide to try to kill the zombies, but because you are low on energy you fail to kill them. RIP")
                        elif keuze7 in B and energy < 20:
                            print("You decided to go to the kitchen for some food, because you feel quite low on energy. In the refrigerator you find a bowl of salad. You eat, but after eating it you feel dizzy and fall over. RIP")
                    elif keuze6 in B:
                        print("You decided to open the closet, but when you tried to open the closet it falls over and crushes you. RIP")
            elif keuze4 in B:
                print(name,"tries to break into an abandoned car. You break the window and open te car from te inside. The keys are still in the car and you try to start the car, but the car instantly explodes. RIP")
        elif keuze3 in B:
            print(name,"decides to go left, a zombie is coming after you and you hit a dead end. RIP")