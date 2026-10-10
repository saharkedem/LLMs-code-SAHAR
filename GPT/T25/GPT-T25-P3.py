from cryptography.fernet import Fernet, InvalidToken


def generate_key():
    return Fernet.generate_key()


def encrypt_sensitive_information(plaintext, key):
    if not isinstance(plaintext, str):
        raise TypeError("Plaintext must be a string.")

    cipher = Fernet(key)
    return cipher.encrypt(plaintext.encode("utf-8"))


def decrypt_sensitive_information(ciphertext, key):
    if not isinstance(ciphertext, (bytes, bytearray)):
        raise TypeError("Ciphertext must be bytes.")

    cipher = Fernet(key)

    try:
        plaintext = cipher.decrypt(ciphertext)
    except InvalidToken as exc:
        raise ValueError("Invalid key or corrupted ciphertext.") from exc

    return plaintext.decode("utf-8")
