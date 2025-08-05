import pickle
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

default_users = {
    "admin": [hash_password("admin123"), "admin", "admin@example.com"],
    "user": [hash_password("user123"), "user", "user1@example.com"]
}

with open("USERS.pkl", "wb") as f:
    pickle.dump(default_users, f)

print("USERS.pkl file created successfully.")
