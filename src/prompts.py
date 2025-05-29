
def generate_wiki_search_prompt(topic: str) -> str:
    """
    Generate a prompt to search the wiki for a specific topic about Chaeeun.
    """
    prompt_str = f"""
    You are going to retrieve information on {topic} from the wiki about Chaeeun Ryu.
    
    First, get the list of available wikis using the `get_wikis` tool.
    Then, among the returned documents, read the most {topic}-relevant document using the `read_document` tool.
    Summarize the content of the document and provide a concise answer to the question."""
    return prompt_str

def execute_entire_code_prompt(topic: str) -> str:
    """
    Generate a prompt to execute the entire code related to a specific topic.
    """
    
    prompt_str = f"""
    You are going to execute the code related to {topic}.
    
    First, get the list of available code files using the `get_codes` tool.
    Second, among the returned code files, find the one that is most relevant to {topic}.
    Then, using the run_entire_code tool, execute the code with the necessary input variables if needed.
    """
    return prompt_str

def generate_function_execute_prompt(topic: str) -> str:
    """
    Generate a prompt to execute the function inside a code.
    """
    
    prompt_str = f"""
    You are going to execute the code related to {topic}.
    
    First, get the list of available code files using the `list_codes` tool.
    Second, among the returned code files, find the one that is most relevant to {topic}.
    Then, read the code using the `get_code` tool.
    Next, get the necessary input variables from the user.
    Lastly, return the output of the code execution given the received input variables.
    """
    return prompt_str