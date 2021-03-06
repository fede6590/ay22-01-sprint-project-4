import os
import hashlib

def allowed_file(filename):
    """
    Checks if the format for the file received is acceptable. For this
    particular case, we must accept only image files.

    Parameters
    ----------
    filename : str
        Filename from werkzeug.datastructures.FileStorage file.

    Returns
    -------
    bool
        True if the file is an image, False otherwise.
    """

    ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
    _, ext = os.path.splitext(filename)
    ext = ext.lower() 

    return ext in ALLOWED_EXTENSIONS


def get_file_hash(file):
    """
    Returns a new filename based on the file content using MD5 hashing.
    It uses hashlib.md5() function from Python standard library to get
    the hash.

    Parameters
    ----------
    file : werkzeug.datastructures.FileStorage
        File sent by user.

    Returns
    -------
    str
        New filename based in md5 file hash.
    """

    hash_id = hashlib.md5(file.read()).hexdigest()
    _, ext = os.path.splitext(file.filename)
    ext = ext.lower()
    hash_name = f"{hash_id}{ext}"
    file.seek(0)
    
    return hash_name