age=int(input("write your age : "))
license=input("Do you have a license? choose (yes) or (no): ")
if age > 18 and license.lower( )=='yes':
    print("you can drive")
else:
    print("sorry,you can not drive")    