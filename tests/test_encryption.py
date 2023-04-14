import unittest
from passprotector.encryption import encrypt, decrypt

#TODO: write the test for encryption.py module
class EncryptionTestCase(unittest.TestCase): # class that defines a collection of individual test methods.
    def test_encrypt_decrypt(self):
        #TODO: add more functionality
        plaintext = b"let's test our cipher" # In Python, a byte string is denoted
        key= b"secretkey"                    # by adding the character 'b' before the start of the string. 
        ciphertext = encrypt(plaintext, key)
        decrypted_plaintext = decrypt(ciphertext, key)
        self.assertEqual(plaintext, decrypted_plaintext)
        """
        self.assertEqual() is an assertion method in the unittest library 
        that verifies that the actual result of a test matches the expected result. 
        In the line above, this method is used to compare the plaintext variable 
        (which is the original message) to the decrypted_plaintext variable 
        (which is the decrypted message). If they match, the test passes. 
        If they don't match, the test fails and an error message is displayed. 
        This is a common way to verify the correctness of a function's output.
        """


    """def test_invalid_inputs():
        #TODO: add more functionality"""
    

# To run (in case you have issues): 
# export PYTHONPATH="${PYTHONPATH}:/Users/username/Documents/GitHub/PassProtectorPy"
# python -m unittest -v test_encryption.py
# python3 -m pip install cryptography
# /usr/bin/python3 -m unittest -v test_encryption.py