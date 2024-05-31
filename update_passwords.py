# update_passwords.py
#!/usr/bin/python3

from flask_bcrypt import Bcrypt
from models import Customer
from database import session

bcrypt = Bcrypt()

def update_passwords():
    users = session.query(Customer).all()
    for user in users:
        new_password = 'new_password_for_user'
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        user.password = hashed_password
    session.commit()

if __name__ == "__main__":
    update_passwords()
    print("Passwords updated successfully.")
