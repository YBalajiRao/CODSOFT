import random 
import string 
def generate_password(length, char_sets):
    all_chars = ''.join(char_set for char_set, include in char_sets.items() if include)
    return ''.join(random.choice(all_chars)for _ in range(length))
def password_generator():
    print("password generator")
    while True:
        length_input = input("Enter the desired length of the password: ")
        if length_input.isdigit() and int(length_input) > 0:
            length = int(length_input)
            break
        else:
            print("Invalid input. Please enter a valid positive integer.")

    char_sets = {c: input(f"Include {c} letters? (yes/no): ").lower() == 'yes' for c in ('lowercase', 'uppercase', 'digits', 'punctuation')}
    if not any(char_sets.values()):
        print("Error: At lease one character set should be included.")
    else: print(f"Generated pasword: {generate_password(length,char_sets)}")
if __name__== "__main__":
    password_generator()    

