def markdown_to_blocks(markdown):
    """
    Split a raw markdown string into blocks separated by double newlines.
    
    Args:
        markdown: A raw markdown string representing a full document
        
    Returns:
        A list of block strings with whitespace stripped and empty blocks removed
    """
    # Split by double newlines
    blocks = markdown.split("\n\n")
    
    # Strip whitespace and filter out empty blocks
    non_empty_blocks = [block.strip() for block in blocks if block.strip()]
    
    return non_empty_blocks