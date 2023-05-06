import os

def read_file(file_path):
    "'""Read data from a file and return it as a string."""
    with open(file_path, 'r') as file: # 'r': read mode ; # 1. 'with' statement allows us to create a context in which the file is open, 
                                                          # and once the context is exited, the file is automatically closed.
                                                          # 2. The 'as' keyword in Python is used to create an alias
        data = file.read()
    return data

def write_file(file_path, data):
    """Write data to a file given a file path and data to write."""
    with open(file_path, 'w') as file: # 'w' : write mode
        file.write(data)

def file_exists(file_path):
    """Check if the file exists."""
    return os.path.isfile(file_path)

def create_file(file_path):
    """Create a new file given a file path."""
    with open(file_path, 'w') as file: # 'w' : write mode
        file.write("") # remember that here we create it

def delete_file(file_path):
    """Delete a file given a file path."""
    os.remove(file_path)