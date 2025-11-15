import pandas as pd
import os

USER_FILE = "users.csv"

def signup(username, password):
    if os.path.exists(USER_FILE):
        users = pd.read_csv(USER_FILE)
    else:
        users = pd.DataFrame(columns=["username", "password"])

    # Check if user exists
    if username in users["username"].values:
        return False  # user already exists

    # Add new user
    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv(USER_FILE, index=False)
    return True


def login(username, password):
    if not os.path.exists(USER_FILE):
        return False  # no users yet

    users = pd.read_csv(USER_FILE)
    valid = ((users["username"] == username) & (users["password"] == password)).any()
    return bool(valid)
