import hashlib

def get_file_hash(file_path):
    block_size = 65536
    file_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        fb = f.read(block_size)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(block_size)
    return file_hash.hexdigest()

def compareHashes(file1, file2):
    ret = "Files are identical" if get_file_hash(file1) == get_file_hash(file2) else "Files are unidentical"
    return ret