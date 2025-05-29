import os
from typing import List
from mcp.server.fastmcp import FastMCP
from src.wiki_tools import *


instructions_str = f"This server answers information about Chaeeun Ryu and executees codes implemented by Chaeeun Ryu.\n"
mcp = FastMCP(name = "MCP Server for Chaeeun Ryu", instructions=instructions_str)

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

