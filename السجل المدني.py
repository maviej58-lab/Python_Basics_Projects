is_egyptian=input('Are you Egyptian? Type "yes" or "No": ').lower( )
if is_egyptian=="yes":
    print("good,that is the first step")
    is_18=input("Are you above 18? Type 'yes' or 'No' : ").lower( )
    if is_18=="yes":
        print('you can have an ID')
    else:
         print("sorry, you have to be 18 or older")   
         print("please try again when you are 18")   
else:
    print('sorry, an Egyptian ID is give only to egyptians')         