#!/usr/bin/env python3
import secrets


def generate_secret(length=64):
    return secrets.token_hex(length // 2)


if __name__ == "__main__":
    new_secret = generate_secret()
    print(new_secret)
