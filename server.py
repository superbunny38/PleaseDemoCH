import os
from typing import List
from mcp.server.fastmcp import FastMCP
from src.wiki_tools import *
from src.prompts import *
from src.code_tools import *

instructions_str = f"This server answers information about Chaeeun Ryu and executes codes implemented by Chaeeun Ryu.\n"
mcp = FastMCP(name = "MCP Server for Chaeeun Ryu", instructions=instructions_str)


# wiki-related tools
@mcp.tool()
def get_wikis() -> List:
    """
    Get the list of wikis available in the server.
    
    Returns:
        A list of wiki file names.
    """
    directory_path = "/Users/chaeeunryu/Desktop/MCP Study/PLEASEPLEASE/wiki"
    return get_files_in_directory(directory_path)

@mcp.tool()
def read_document(file_name: str) -> str:
    """
    Read the content of a wiki document.
    
    Args:
        file_name: The name of the file to read.
    
    Returns:
        The content of the document as a string.
    """
    directory_path = "/Users/chaeeunryu/Desktop/MCP Study/PLEASEPLEASE/wiki"
    html_path = os.path.join(directory_path, file_name)
    return get_document(html_path)

# code-related tools
@mcp.tool()
def get_codes() -> List[str]:
    """
    Get the list of code files available in the server.
    
    Returns:
        A list of code file names.
    """
    directory_path = "/Users/chaeeunryu/Desktop/MCP Study/PLEASEPLEASE/codes"
    return get_codes_in_directory(directory_path, extensions=['.py', '.cpp'])

@mcp.tool()
def run_entire_code(file_name: str) -> str:
    """
    Execute a code file with the provided input variables.
    
    Args:
        file_name: The name of the code file to execute.
        input_variables: A dictionary of input variables for the code.
    
    Returns:
        The output of the executed code or an error message if execution fails.
    """
    directory_path = "/Users/chaeeunryu/Desktop/MCP Study/PLEASEPLEASE/codes"
    file_path = os.path.join(directory_path, file_name)
    return execute_entire_cpp(file_path)

@mcp.tool()
def get_code(file_name: str) -> str:
    """
    Retrieve the content of a code file.
    
    Args:
        file_name: The name of the code file to retrieve.
    
    Returns:
        The content of the code file as a string.
    """
    directory_path = "/Users/chaeeunryu/Desktop/MCP Study/PLEASEPLEASE/codes"
    file_path = os.path.join(directory_path, file_name)
    return get_code(file_path)

# prompts
@mcp.prompt()
def generate_wiki_prompt(topic: str) -> str:
    """
    Generate a prompt to search the wiki for a specific topic about Chaeeun.
    
    Args:
        topic: The topic to search for in the wiki.
    
    Returns:
        A formatted prompt string.
    """
    return generate_wiki_search_prompt(topic)

@mcp.prompt()
def run_function_prompt(topic: str) -> str:
    """
    Generate a prompt to execute the function inside a code.
    
    Args:
        topic: The topic to search for in the code.
    
    Returns:
        A formatted prompt string.
    """
    return generate_function_execute_prompt(topic)

@mcp.prompt()
def test_entire_code_execution(topic: str) -> str:
    """
    Generate a prompt to execute the function inside a code.
    
    Args:
        topic: The topic to search for in the code.
    
    Returns:
        A formatted prompt string.
    """
    return execute_entire_code_prompt(topic)

if __name__ == "__main__":
    # Run the server
    mcp.run(transport='stdio')