import os

def list_only_dirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_only_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    return os.listdir(path)
