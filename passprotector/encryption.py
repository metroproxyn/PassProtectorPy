import hashlib
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.fernet = Fernet(self.key)
    
    def encrypt(self, password):
        encrypted_password = self.fernet.encrypt(password.encode())
        return encrypted_password
    
    def decrypt(self, encrypted_password):
        decrypted_password = self.fernet.decrypt(encrypted_password)
        return decrypted_password