from cryptography.fernet import Fernet


def generate_encryption_key():
    return Fernet.generate_key()


def encrypt_sensitive_text(text, key):
    cipher = Fernet(key)
    return cipher.encrypt(text.encode("utf-8"))


def decrypt_sensitive_text(encrypted_value, key):
    cipher = Fernet(key)
    decrypted_value = cipher.decrypt(encrypted_value)
    return decrypted_value.decode("utf-8")
