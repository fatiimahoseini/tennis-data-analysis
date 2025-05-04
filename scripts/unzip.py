import os
import zipfile

# Extracts the contents of a zip file to the specified directory.
def extract_zip_file(zip_path, extract_to=None):
    """
    Parameters:
    zip_path (str): The path to the zip file.
    extract_to (str): The directory where the contents should be extracted. 
    If None, contents will be extracted in the zip file's directory.
    """
    if extract_to is None:
        extract_to = os.path.dirname(zip_path)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted all files to: {extract_to}")

extract_zip_file("../data/tennis_data.zip", "../data")