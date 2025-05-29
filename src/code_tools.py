import os
from typing import List
import subprocess

def execute_entire_cpp(file_path: str) -> str:
    """
    Compile and execute a C++ file.

    Args:
        file_path (str): The path to the C++ file.

    Returns:
        str: The output of the execution, or an error message if compilation or execution fails.
    """
    if not os.path.exists(file_path):
        return f"Error: The file '{file_path}' does not exist."
    
    if not os.path.isfile(file_path):
        return f"Error: The path '{file_path}' is not a file."
    
    if not file_path.endswith(".cpp"):
        return f"Error: The file '{file_path}' is not a C++ file."

    # Get the directory and file name without extension
    directory = os.path.dirname(file_path)
    executable_name = os.path.splitext(os.path.basename(file_path))[0]
    executable_path = os.path.join(directory, executable_name)

    try:
        # Compile the C++ file
        compile_command = ["g++", file_path, "-o", executable_path]
        compile_result = subprocess.run(compile_command, capture_output=True, text=True)

        if compile_result.returncode != 0:
            return f"Compilation failed:\n{compile_result.stderr}"

        # Execute the compiled file
        execute_command = [executable_path]
        execute_result = subprocess.run(execute_command, capture_output=True, text=True)

        if execute_result.returncode != 0:
            return f"Execution failed:\n{execute_result.stderr}"

        return execute_result.stdout
    except Exception as e:
        return f"Error during compilation or execution: {e}"

def get_code(file_path: str) -> str:
    """
    Retrieve the content of a code file given its file path.

    Args:
        file_path (str): The path to the code file.

    Returns:
        str: The content of the code file as a string, or an error message if the file cannot be read.
    """
    if not os.path.exists(file_path):
        return f"Error: The file '{file_path}' does not exist."
    
    if not os.path.isfile(file_path):
        return f"Error: The path '{file_path}' is not a file."
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading the file: {e}"


def get_codes_in_directory(directory_path: str, extensions: List[str] = None) -> List[str]:
    """
    Get the list of code files in the specified directory based on file extensions.

    Args:
        directory_path (str): The path to the directory.
        extensions (List[str]): A list of file extensions to filter by (e.g., ['.py', '.cpp']).
                                If None, all files are returned.

    Returns:
        List[str]: A list of code file names in the directory.
    """
    if not os.path.exists(directory_path):
        return [f"Error: The directory '{directory_path}' does not exist."]
    
    if not os.path.isdir(directory_path):
        return [f"Error: The path '{directory_path}' is not a directory."]
    
    try:
        # List all files in the directory with the specified extensions
        files = [
            file for file in os.listdir(directory_path)
            if os.path.isfile(os.path.join(directory_path, file)) and
               (extensions is None or os.path.splitext(file)[1] in extensions)
        ]
        return files
    except Exception as e:
        return [f"Error reading the directory: {e}"]
    
