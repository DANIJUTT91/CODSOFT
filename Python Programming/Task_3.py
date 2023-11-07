import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

p_len = 8
try:
    p_len = int(input("Enter a positive integer as the length of password you want: "))
    if(p_len<1):
        print("Password should be positive integer")
except:
    print("Invalid input")

print('Here\'s a random password of',p_len,generate_password(p_len))