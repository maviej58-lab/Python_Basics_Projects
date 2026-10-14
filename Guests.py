guests=["Ramy", "Taha", "Sameh", "Janna"]
name=input("Please enter your name: ").capitalize()
if name in guests:
    print(f"Good to see you,{name} \nWelcome to the party")
else:
    print(f"sorry, couldn't find the name {name} on our list")