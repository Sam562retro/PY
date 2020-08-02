import hashlib
import os


password = input("please enter your password:  ")
salt = os.urandom(32)
salt_password = (str(salt) + password)
print("salt + password:\n")
print(salt_password)
print("\nsalt:\n\n")
print(salt)
print("\nencoded password:\n")
print("salted one:\n")
print(salt_password.encode('utf8'))
print("\nwithout salting:\n")
print(password.encode("utf8"))
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt,100000)
print("\n\nhashed and salted pasword:\n\n\n")
print(key)
