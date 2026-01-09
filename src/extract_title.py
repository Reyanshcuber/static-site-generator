def extract_title(markdown):
    """
    Extract the h1 header from a markdown string.
    
    Args:
        markdown: A string containing markdown content
        
    Returns:
        The title text without the # and any leading/trailing whitespace
        
    Raises:
        Exception: If no h1 header is found
    """
    lines = markdown.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('# ') and not line.startswith('## '):
            # Found h1 header, extract the title
            title = line[2:].strip()
            return title
    
    # No h1 header found
    raise Exception("No h1 header found in markdown")
