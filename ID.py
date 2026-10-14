names=input("Enter the first name ........;").split(", ")
new=[ ]
for x in names:
    parts=x.split(" ")
    new.append(parts)
    print(parts)
print("Abbreviated Names: ")
for name in new:
    print(name[0][0]+" . "+name[1][0]+" . ")    