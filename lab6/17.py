import os

def list_only_dirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_only_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    return os.listdir(path)

def check_access(path):
    return {
        "Exists": os.path.exists(path),
        "Readable": os.access(path, os.R_OK),
        "Writable": os.access(path, os.W_OK),
        "Executable": os.access(path, os.X_OK)
    }