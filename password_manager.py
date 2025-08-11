# Import the Fernet class from the cryptography.fernet module for symmetric encryption
from cryptography.fernet import Fernet

'''
# Function to generate and save a new encryption key to a file
def write_key():
    # Generate a new Fernet key
    key = Fernet.generate_key()
    # Save the generated key into a binary file named "key.key"
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


# Function to load the existing encryption key from the file
def load_key():
    # Open the key file in read-binary mode
    file = open("key.key", "rb")
    # Read the key from the file
    key = file.read()
    # Close the file after reading
    file.close()
    # Return the key to be used for encryption/decryption
    return key


# Load the encryption key from the file
key = load_key()
# Create a Fernet object with the loaded key to handle encryption/decryption
fer = Fernet(key)


# Function to view all saved usernames and passwords
def view():
    # Open the password storage file in read mode
    with open('passwords.txt', 'r') as f:
        # Read all lines from the file
        for line in f.readlines():
            # Remove trailing newline characters
            data = line.rstrip()
            # Split the line into username and encrypted password
            user, passw = data.split("|")
            # Decrypt the password and display it alongside the username
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


# Function to add a new username and password
def add():
    # Ask the user for the account name
    name = input('Account Name: ')
    # Ask the user for the password
    pwd = input("Password: ")

    # Open the password file in append mode
    with open('passwords.txt', 'a') as f:
        # Encrypt the password, decode it to string, and save with username
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


# Main program loop
while True:
    # Ask the user whether they want to add, view, or quit
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    
    # If the user types 'q', exit the loop
    if mode == "q":
        break

    # If the user chooses 'view', display saved passwords
    if mode == "view":
        view()
    # If the user chooses 'add', allow them to save a new password
    elif mode == "add":
        add()
    # If the input doesn't match, show an error and continue the loop
    else:
        print("Invalid mode.")
        continue
