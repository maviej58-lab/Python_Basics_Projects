print("welcome to 'whose wallet?' ")
print("you will give me a list of names, and i will pick a person to pay")
names_string=input("if you 're ready , enter the names separated by a comma ...")
names=names_string.split(", ")
length=len(names)
random1=random.randint(1,length)
if random1==1:
    print("please ask" ,names[0] ,"to take his wallet out. dinner is on him")
elif random1==length:
    print("please ask" ,names[-1] ,"to take his wallet out. dinner is on him")    
elif random1<length :
    print("please ask" ,names[2] ,"to take his wallet out. dinner is on him")    