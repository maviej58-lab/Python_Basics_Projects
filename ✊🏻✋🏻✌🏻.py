import random
Rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
Paper =( '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
Scissors =( '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
game=[Rock, Paper, Scissors]
choices=["Rock", "Paper", "Scissors"]
computer=random.choice(game)
print("Welcome to the Rock, Paper, Scissors game")
output=input("press Enter to continue or Type(Help) for the rules").lower()
if output=="help":
    print("       ★★★Rules★★★       \n1)you choose and the computer chooses  \n2)Rock smashes Scissors-> Rock wins  \n3)scissors cut paper-> scissors win   \n4)paper covers Rock -> paper wins")
    choise=input("Enter your choice(Rock, Paper, Scissors): ").capitalize()
    print("you chose: \n")
    if choise == "Rock":
        print(Rock)

    elif choise == "Paper":
        print(Paper)

    elif choise == "Scissors":
        print(Scissors)

    else:
        print("Invalid choice")
    if choise in choices:
        print(f" \nComputer chose: \n{computer}")
    else:
        print("Invalid choice. please run the program again and choose Rock, paper, scissors")   
else:
     choise=input("Enter your choice(Rock, Paper, Scissors): ").capitalize()
     print("you chose: \n")
     if choise == "Rock":
        print(Rock)

     elif choise == "Paper":
        print(Paper)

     elif choise == "Scissors":
        print(Scissors)

     else:
        print("Invalid choice")
     if choise in choices:
        print(f" \nComputer chose: \n{computer}")
     else:
        print("Invalid choice. please run the program again and choose Rock, paper, scissors")   
        
     