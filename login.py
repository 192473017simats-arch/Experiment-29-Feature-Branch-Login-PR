def login(username: str, password: str) -> bool:
    valid_users = {"mohith": "simats@2026", "admin": "admin123"}
    return valid_users.get(username) == password

if __name__ == "__main__":
    print("Valid login:", login("mohith", "simats@2026"))
    print("Invalid login:", login("mohith", "wrong"))
