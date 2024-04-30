#!/usr/bin/env python3
import argparse
import logging
from passlib.context import CryptContext

# Surpress the warning message from passlib.
logging.getLogger("passlib").setLevel(logging.ERROR)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):
    """Hash a password."""
    return pwd_context.hash(password)


def verify_password(password, hashed):
    """Verify a password against a given hash."""
    return pwd_context.verify(password, hashed)


def main():
    parser = argparse.ArgumentParser(
        description="Hash and verify passwords using bcrypt."
    )
    subparsers = parser.add_subparsers(dest="command", help="commands")

    hash_parser = subparsers.add_parser("hash", help="Hash a password")
    hash_parser.add_argument("password", type=str, help="Password to hash")

    args = parser.parse_args()

    if args.command == "hash":
        print(f"Password to be hashed: {args.password}")
        hashed_password = hash_password(args.password)
        print(f"Hashed password: {hashed_password}")
        result = pwd_context.verify(args.password, hashed_password)
        print("Password is correct:" if result else "Password is incorrect.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
