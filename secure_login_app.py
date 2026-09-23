import os
import hashlib

stored_username = os.getenv("APP_USERNAME", "admin")
stored_password_hash = hashlib.sha256(
    os.getenv("APP_PASSWORD", "admin123").encode()
).hexdigest()

username = input("Enter username: ")
password = input("Enter password: ")

password_hash = hashlib.sha256(password.encode()).hexdigest()

if username == stored_username and password_hash == stored_password_hash:
    print("Login successful")
else:
    print("Invalid username or password")