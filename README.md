# Hash My Password 🔐

Simple password hashing script using bcrypt

- https://passlib.readthedocs.io/en/stable/install.html

Create venv

```bash
python3 -m venv .venv;source .venv/bin/activate
```

Install lib

```bash
pip install -r requirements.txt
```

Check lib

```bash
python -c "from passlib.context import CryptContext; print('Passlib is installed!')"
```

Make executable

```bash
chmod +x hash_mypwd.py
```
