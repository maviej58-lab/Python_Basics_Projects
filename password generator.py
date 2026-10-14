print("welcome to the password generator!")
character=int(input("Enter the total number of characters in the password:"))
letters=int(input("Enter the number of letters in the password:"))
numbers=int(input("Enter the number of numbers in the password:"))
symbols=int(input("Enter the number of the symbols in the password:"))
sum=letters+numbers+symbols
if sum!=character:
    print("invalid input. the sum of letters, numbers, and symbols doesn't match the password")
else:
    import random
    import string
    number=["0", "1", "2", "3", "4", "5," "6", "7", "8", "9"]
    Number=random.choices(number, k=numbers)
    letter=random.choices(string.ascii_letters, k=letters)
    symbol=random.choices(string.punctuation, k=symbols)
    password=[]  
    password.extend(Number)
    password.extend(letter)
    password.extend(symbol)
    random.shuffle(password)
    print("Generated password: ")
    print("".join(password)) 