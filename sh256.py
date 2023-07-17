import hashlib
import sys
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path as a command-line argument.")
        sys.exit(1)
    file_path = sys.argv[1]
    sha256 = calculate_sha256(file_path)
    print("SHA256:", sha256)