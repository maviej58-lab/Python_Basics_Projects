print("Welcome to place the rabbit")
field=[["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("where should the rabbit go?🐇")
place=input("please choose a row and a column....")
row=int(place[0])
column=int(place[1])
field[row-1][column-1]="🐇"
print(" \nsuccess...... \n")
print(f"{field[0]} \n{field[1]} \n{field[2]}")