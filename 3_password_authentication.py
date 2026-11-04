# Password authentication system
# I'm just going to simulate a database with a dictionary to store login/password pairs.
# We are not encrypting the passwords, just hashing them for simplicity. In a real-world application, you should use a secure hashing algorithm and store the hashed passwords securely.

import bcrypt

dummy_database = {} 
salt = bcrypt.gensalt()

def hash_password(password:str):
    '''Hash the password using a simple hashing algorithm '''
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def register_user(username, password):
    ''' Register a new user with a username and password '''
    if username in dummy_database:
        return "Username already exists."
    dummy_database[username] = hash_password(password)
    return "User registered successfully."

def verify_password(password:str, salt: bytes ):
    ''' Verify the password against the stored hash '''
    return bcrypt.checkpw(password.encode('utf-8'), salt)

def login_user(username, password):
    ''' Authenticate a user with a username and password '''
    if username not in dummy_database:
        return "User not found."
    if verify_password(password, dummy_database[username]):
        return "Login successful."
    return "Invalid password."

def delete_account(username):
    ''' Delete an existing user account '''
    if username in dummy_database:
        del dummy_database[username]
        return "Account deleted successfully."
    return "User not found."


# Obviously more testing would be needed, I'm trying to keep it simple. 
print(register_user("user1", "password123"))
print(login_user("user1", "password123"))