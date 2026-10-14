import string
def solve(message, shift):
    alphabet=string.ascii_lowercase
    
    solve_message=" "  
    for letter in message:
        if letter.lower() in alphabet:
            original_position=alphabet.index(letter.lower())
            new_position=(original_position-shift)%26
            solve_letter=alphabet[new_position]
            if letter.isupper():
                solve_letter=solve_letter.upper()
            solve_message+=solve_letter
        else:
            solve_message+=letter
    print(solve_message)
user_message=input("Enter a message: ")
shift_number=int(input("Enter a shift number: "))
solve(user_message, shift_number)                                            