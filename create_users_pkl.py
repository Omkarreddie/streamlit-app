import pickle
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

default_users = {
    "Here you can add your default users
}

with open("USERS.pkl", "wb") as f:
    pickle.dump(default_users, f)

print("USERS.pkl file created successfully.")
