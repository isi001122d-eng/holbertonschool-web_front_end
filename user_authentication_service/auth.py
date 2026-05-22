#!/usr/bin/env python3
"""
Authentication helper functions module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Returns a salted bcrypt hash of the input password
    """
    # 1. String tipli parolu bayta çeviririk
    password_bytes = password.encode('utf-8')

    # 2. Təhlükəsiz random duz (salt) generasiya edirik
    salt = bcrypt.gensalt()

    # 3. Parolu heşləyib bayt formatında geri qaytarırıq
    return bcrypt.hashpw(password_bytes, salt)
