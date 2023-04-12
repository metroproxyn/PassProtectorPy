# PassProtectorPy

PassProtectorPy is a password manager project written in Python. It allows users to securely store their passwords and other sensitive information in an encrypted format. The project will have the following structure:

```
PassProtectorPy/
├── docs/
├── passprotector/
│   ├── __init__.py
│   ├── encryption.py
│   ├── file_handling.py
│   ├── user_interface.py
├── tests/
│   ├── test_encryption.py
│   ├── test_file_handling.py
│   ├── test_user_interface.py
├── .gitignore
├── LICENSE
├── README.md
└── setup.py
```

1. docs/ folder: This folder will contains the documentation for the project (TBS)
2. passprotector/ folder: This folder contains the source code (src) for the project. 
    - init.py: A blank file to mark this directory as a Python package.
    - encryption.py: Contains functions for encrypting and decrypting data.
    - file_handling.py: Contains functions for reading from and writing to files.
    - user_interface.py: Contains functions for interacting with the user through the command line.
3. tests/ folder:
    - test_encryption.py: testing the encryption and decryption functionality.
    - test_file_handling.py: testing the file handling functionality.
    -  test_user_interface.py: testing the user interface functionality.

The basic functionalities of the project will include:

- Creating a master password for the user to access the password manager.
- Adding a new login information such as username, password and website URL to the password manager.
- Viewing saved login information.
- Updating login information.
- Deleting login information.
- Generating strong passwords for the user.

The project uses the cryptography library for encryption and decryption of user data.

PassProtectorPy is managed using GitHub and has a project board to keep track of tasks and issues.