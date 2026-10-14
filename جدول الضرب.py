print("     ★★★Welcome to the multiplication table★★★     ")
number=input("Enter a number: ")
print(f"multiplication table for {number} ")
for i in range(1,11):
    result=int(number)*i
    print(f"{int(number)}*{int(i)}={result}")