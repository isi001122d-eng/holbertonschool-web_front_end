#!/usr/bin/env python3
"""
Authentication module containing helper functions and the Auth class.
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB


def _hash_password(password: str) -> bytes:
    """
    Returns a salted bcrypt hash of the input password string.

    Args:
        password (str): The plain-text password to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initialize a new Auth instance with a private DB session.
        """
        self._db = DB()

    def register_user(self, email: str, password: str):
        """
        Registers a new user if they do not already exist in the database.

        Args:
            email (str): The user's email address.
            password (str): The user's plain-text password.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If the user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password).decode('utf-8')
            return self._db.add_user(email, hashed_password)
