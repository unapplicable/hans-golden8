import re

def normalize(username):
    return username.strip().lower()

def validate(username, password):
    if len(password) < 8:
        raise ValueError("password too short")
    return True
