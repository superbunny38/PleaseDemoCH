
def generate_wiki_search_prompt(topic: str) -> str:
    """
    Generate a prompt to search the wiki for a specific topic about Chaeeun.
    """
    prompt_str = """
    You are going to retrieve information on {topic} from the wiki about Chaeeun Ryu.
    
    First, get the list of available wikis using the `get_wikis` tool.
    Then, among the returned documents, read the most {topic}-relevant document using the `read_document` tool.
    Summarize the content of the document and provide a concise answer to the question."""
    return prompt_str