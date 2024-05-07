# Hash My Password 🔐

Generating Secrets and Hashing

## Getting started

Create virtual envirnonment:

```bash
python3 -m venv .venv;source .venv/bin/activate
```

Install modules:

```bash
pip install -r requirements.txt
```

## Generate client secret using secrets module

The secrets module provides secure random number generation suitable for cryptographic purposes. It is designed to be used in scenarios where randomness is critical for security, such as generating authentication tokens, session keys, or password reset codes.

Usage:

```bash
python generate-secret.py
```

Output:

```bash
9c10b72b5e866507837d5d4958533e628c4cd63b80da0c1376bcd193dc6bafb3
```

## Simple password hashing script using bcrypt module

This script provides a simple way to securely hash and verify passwords using the bcrypt module. The hashed passwords can be stored in a database or file, and when a user provides a password, you can compare it with the stored hashed password to verify its validity.

- <https://passlib.readthedocs.io/en/stable/install.html>

Check:

```bash
python -c "from passlib.context import CryptContext; print('Passlib is installed!')"
```

Usage:

```bash
python hash_mypwd.py hash 9c10b72b5e866507837d5d4958533e628c4cd63b80da0c1376bcd193dc6bafb3
```

Output:

```bash
Password to be hashed: 9c10b72b5e866507837d5d4958533e628c4cd63b80da0c1376bcd193dc6bafb3
Hashed password: $2b$12$vQNuEjJIhgEiLAZul8cT/.NtrnxvrcqBBHWRsbinp6bPaRzA5nwtW
```
