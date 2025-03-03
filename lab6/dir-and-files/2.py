import os
path = input("enter the path:")
if os.path.exists(path):
    print("exists:")
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
else:
    print("does not exist")