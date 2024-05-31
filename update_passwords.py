# update_passwords.py
#!/usr/bin/python3

from flask_bcrypt import Bcrypt
from models import Customer
from database import session

bcrypt = Bcrypt()

def update_passwords():
    users = session.query(Customer).all()
    for user in users:
        # Assuming you have a way to retrieve or reset the user's password
        new_password = 'new_password_for_user'  # Replace with actual password retrieval logic
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        user.password = hashed_password
    session.commit()

if __name__ == "__main__":
    update_passwords()
    print("Passwords updated successfully.")
