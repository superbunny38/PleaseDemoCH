import os
from typing import List

def get_document(html_path: str) -> str:
    """
    Retrieve the content of a document given its HTML file path.
    
    Args:
        html_path: The path to the HTML file.
    
    Returns:
        The content of the document as a string, or an error message if the file cannot be read.
    """
    if not os.path.exists(html_path):
        return f"Error: The file at path '{html_path}' does not exist."
    
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading the file: {e}"

def get_files_in_directory(directory_path: str) -> List[str]:
    """
    Get the list of files in the specified directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        List[str]: A list of file names in the directory.
    """
    if not os.path.exists(directory_path):
        return [f"Error: The directory '{directory_path}' does not exist."]
    
    if not os.path.isdir(directory_path):
        return [f"Error: The path '{directory_path}' is not a directory."]
    
    try:
        # List all files in the directory
        files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
        return files
    except Exception as e:
        return [f"Error reading the directory: {e}"]

