import hashlib

BLOCK_SIZE = 4096 

path = "./website/static/files/"

def secureHashing(file):
    hash = hashlib.sha256() 
    with open(file, 'rb') as f: 
        fb = f.read(BLOCK_SIZE) 
        while len(fb) > 0: 
            hash.update(fb) 
            fb = f.read(BLOCK_SIZE) 
    fileName = list(file.split("/"))[-1]
    outputFileName = fileName.split(".")[0] + "_hash.txt" 
    hash_file = path + outputFileName
    with open (hash_file, "w") as output:
        output.write(hash.hexdigest())
    return outputFileName