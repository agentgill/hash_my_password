#!/usr/bin/env python3
import secrets


def generate_secret(length=64):
    """
    Generate a secure random hexadecimal string.

    Parameters:
    length (int): The length of the hexadecimal string to generate.
                  Must be an even number.

    Returns:
    str: A securely generated random hexadecimal string.
    """
    if length % 2 != 0:
        raise ValueError("Length must be an even number.")
    return secrets.token_hex(length // 2)


def main():
    # Generate client_id (32-character hexadecimal string)
    client_id = generate_secret(length=32)
    print(f"Client ID: {client_id}")

    # Generate client_secret (64-character hexadecimal string)
    client_secret = generate_secret(length=64)
    print(f"Client Secret: {client_secret}")


if __name__ == "__main__":
    main()
