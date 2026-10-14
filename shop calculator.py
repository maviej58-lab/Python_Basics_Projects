print("    ★★Welcome to iShop calculater★★    ")
no1=int(input("How many items are there in your basket today?..."))
print("let's get to counting them...")
cost=[ ]
basket=[ ]
for i in range(1,no1+1):
    x=input(f"please tell me the name of the item number{i}")
    y=input(f"what is the price of {x}$")
    cost.append(float(y))
    basket.append(x)
z=input("would you like to see your entire basket items?").lower()   
if z=="yes":
    print(basket) 
f=input("would you like to see how much it'll cost?").lower()   
if f=="yes":
    print(f"Buying these items will cost:{sum(cost)}$") 