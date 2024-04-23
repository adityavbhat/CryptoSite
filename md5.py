import hashlib

BLOCK_SIZE = 4096

path = "./website/static/files/"

def secure_hashing_md5(file):
    hash = hashlib.md5()  # Create an MD5 hash object
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    
    # Extract file name from the path
    file_name = list(file.split("/"))[-1]
    # Create output file name based on the input file name
    output_file_name = file_name.split(".")[0] + "_md5_hash.txt"
    # Define the full path for the output file
    hash_file = path + output_file_name
    
    # Write the hash digest to the output file
    with open(hash_file, "w") as output:
        output.write(hash.hexdigest())
    
    return output_file_name
