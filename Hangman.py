import random
words=["good", "bad", "ugly"]
random_word=random.choice(words)
stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
choosen_letters=[]
display=["_"]*len(random_word)
print('  '.join(display)) 
lives=6   
while "_"   in display and lives>0:
    guessed=input("please guess a letter: ").lower()
    if guessed in choosen_letters:
        print(f"you already guessed {guessed} ! ")
        print(f"you have {lives} more tries")
        continue
    choosen_letters.append(guessed)  
    if guessed not in random_word:
        lives-=1
    print(f"you have {lives} more tries")
    print(stages[6-lives])
    if lives==0:
        print("Game over! you hung the man. ")
        break
    for position in range(len(random_word)):
        if random_word[position]==guessed:
            display[position]=guessed 
    print(" ".join(display))
if "_" not in display:
    print('''
          ***********
          you win!
          ************
          ''')         