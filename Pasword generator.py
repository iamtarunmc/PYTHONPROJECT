import random
import string
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Here you can have strongest password for yor information,WELCOME!!!")
    length = int(input("Enter the length of the password: "))
    if length == 0:
        print("Thanks for visiting")
    else:
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print("The strongest password:",password)
if __name__ == "__main__":
    main()