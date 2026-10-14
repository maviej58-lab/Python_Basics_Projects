print("👾👾👾?👾")
print("Welcome to my Island!")
print("There are two doors in front of you. 🚪a red door and 🚪a blue door")
door=input("which door do you want to open ? ").lower( )
if door=="red":
    print("Great ! now you entered a room.")
    print('you found three boxes 🎁 white , 🎁 black , 🎁 green')
    box=input("which box do you open?").lower( )
    if box=="green":
        print("Congratulations ! You found the treasure! 💰💰💰")
    elif box=='white':
        print('Oops! you opened a box filled with snaks 🐍🐍🐍🐍')
    elif box=="black" :
         print("Oops! you opened a box filled with spiders🕷️🕸️🕷️🕸️🕷️🕸️")
    else:
         print("Invalid choise!🤷🏻‍♂️❌🤷🏻‍♂️❌🤷🏻‍♂️❌")
elif door=="blue":
    print("Oops! you chose the crocodile door🐊🐊🐊")
    print("Game over!")
else:
    print("Invalid choise!🤷🏻‍♂️❌🤷🏻‍♂️❌🤷🏻‍♂️❌")
    