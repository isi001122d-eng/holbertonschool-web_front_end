#!/usr/bin/env python3
"""
Authentication helper functions and Auth class module
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB


def _hash_password(password: str) -> bytes:
    """
    Returns a salted bcrypt hash of the input password
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)


class Auth:
    """Auth class to interact with the authentication database
    """

    def __init__(self):
        """Initialize a new Auth instance with a private DB session
        """
        self._db = DB()

    def register_user(self, email: str, password: str):
        """Registers a new user if they don't already exist
        """
        try:
            # 1. İstifadəçinin mövcudluğunu yoxlayırıq
            self._db.find_user_by(email=email)
            # Əgər bura keçə bilsə, deməli istifadəçi artıq var -> ValueError fırladırıq
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            # 2. İstifadəçi tapılmadıqda (NoResultFound), qeydiyyatı başladırıq
            hashed_pw_bytes = _hash_password(password)
            # Baytı string-ə çeviririk ki, VARCHAR sütununa düzgün otursun
            hashed_pw_str = hashed_pw_bytes.decode('utf-8')

            # 3. Bazaya əlavə edirik
            new_user = self._db.add_user(email, hashed_pw_str)
            return new_user
