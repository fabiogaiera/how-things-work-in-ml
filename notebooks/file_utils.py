import os
import sys
import uuid

def rename_file(current_path):
    
    path = os.path.dirname(os.path.abspath(current_path))
    name = str(uuid.uuid4()) + ".png"
    new_path = os.path.join(path, name)
    os.rename(current_path, new_path)


if __name__ == "__main__":
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            path_to_file = os.path.join(root, file)
            rename_file(path_to_file)