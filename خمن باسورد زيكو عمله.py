password=input("Enter a 4-digit PIN code:")
import random
correct_password="".join(str(random.randint(0,9))for i in range(4))
if password==correct_password:
    print("Congratulations!")
elif len(password)!=4:
    print("please Enter 4 digits")
else :
    print("failure!PIN code did not match")
    print("The computer generated this pin : " ,{correct_password})
    