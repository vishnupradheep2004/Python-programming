import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("The length of password should be atleast 8 characters.So please enter an integer above 8")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            
    password = generate_password(length)
    print("Generated Password:")
    print(password)

if __name__=="__main__":
    main()
    
