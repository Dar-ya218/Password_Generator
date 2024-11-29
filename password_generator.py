import random
import string
import time

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Create character pool based on user preferences
    char_pool = ""
    if use_letters:
        char_pool += letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols
    
    # Ensure at least one character type is selected
    if not char_pool:
        return "Error: Please select at least one character type!"
    
    # Generate password
    password_characters = []

    for _ in range(length):
        random_character = random.choice(char_pool)
        password_characters.append(random_character)

    password = ''.join(password_characters)
    return password


def password_strength(password):
    """Rate password strength with a fun message"""
    score = 0
    messages = [
        "🌱 A baby could crack this!",
        "🤔 My grandma's birthday was harder to guess...",
        "💪 Not bad, not bad at all!",
        "🔒 Fort Knox is taking notes!",
        "🚀 Even NASA would be proud!"
    ]
    
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    return messages[score]

# Main program
print("🔐 Welcome to the Password Generator 3000! 🔐")
print("Where we turn 'password123' into 'Fort Knox material'!")

while True:
    print("\n🎯 What would you like to do?")
    print("1. 🎲 Generate a new password")
    print("2. 💡 Password strength tips")
    print("3. 🚪 Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '3':
        print("\n🎭 Stay secure, my friend! Remember: 'password' is not a password!")
        break
    
    elif choice == '1':
        print("\n🎨 Let's create your super-secure password!")
        try:
            length = int(input("Password length (8-50): "))
            if not 8 <= length <= 50:
                print("🚫 Length must be between 8 and 50!")
                continue
                
            print("\nInclude:")
            letters = input("Letters? (y/n): ").lower() == 'y'
            numbers = input("Numbers? (y/n): ").lower() == 'y'
            symbols = input("Symbols? (y/n): ").lower() == 'y'
            
            print("\n🤖 Generating your password", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print("\n")
            
            password = generate_password(length, letters, numbers, symbols)
            print(f"🎉 Your new password is: {password}")
            print(f"💪 Strength: {password_strength(password)}")
            
        except ValueError:
            print("🚫 Please enter a valid number!")
            
    elif choice == '2':
        print("\n🌟 Password Pro Tips:")
        print("1. Longer is stronger! Like a good story, but with more symbols.")
        print("2. Mix it up! Letters, numbers, symbols - it's a party in there!")
        print("3. Avoid obvious stuff like 'password123' (Yes, people still do that)")
        print("4. Your pet's name backwards is not as clever as you think")
        print("5. If your password is 'secure123', you're doing it wrong!")
    
    else:
        print("🚫 That's not a valid option! Try again!")