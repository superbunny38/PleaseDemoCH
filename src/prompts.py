
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

def generate_code_execute_prompt(topic: str) -> str:
    """
    Generate a prompt to execute the function inside a code.
    """
    
    prompt_str = f"""
    You are going to execute the code related to {topic}.
    
    First, get the list of available code files using the `list_codes` tool.
    Then, among the returned code files, find the one that is most relevant to {topic}.
    Next, get the input variables from the user using the `get_input_variables` tool.
    Execute the code using the `run_code` tool with the received input variables.
    """
    return prompt_str