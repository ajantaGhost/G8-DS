import hashlib
def hash_file(filename):
    """Return the SHA-1 hash of the file content."""
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = file.read(8192)
        while chunk:
            h.update(chunk)
            chunk = file.read(8192)
    return h.hexdigest()
def compare_pdfs(file1, file2):
    """Compare two PDF files and return whether they are identical."""
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    if hash1 == hash2:
        print("The PDF files are identical.")
    else:
        print("The PDF files are different.")
file1 = "D:/Ajanta_Ghosh/SureTrust/python/document1.pdf"
file2 = "D:/Ajanta_Ghosh/SureTrust/python/document2.pdf"
compare_pdfs(file1, file2)
