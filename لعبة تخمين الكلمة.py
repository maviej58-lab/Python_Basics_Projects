import random
words=["good", "bad", "ugly"]
random_word=random.choice(words)
#اعرض مسافات بنفس عدد حروف الكلمة
display=[]
for letter in random_word:
    display.append("_")
print(display)   
#اطلب تخمين حرف 
while "_" in display:
    guessed=input("please guess a letter: ").lower()
    #لو صح بدل المسافة بالحرف و اكمل 
    for position in range(len(random_word)):
        if random_word[position]==guessed:
            display[position]=guessed
    print(display)
print("""
        ♪♪♪♪♪♪♪
        you win
        ♪♪♪♪♪♪♪
        """)