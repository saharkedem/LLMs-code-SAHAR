from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_text(text, key):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text.encode("utf-8"))
    return encrypted_text


def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text.decode("utf-8")
