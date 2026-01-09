from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    """
    Determine the type of a markdown block.
    
    Args:
        block: A single block of markdown text (whitespace already stripped)
        
    Returns:
        BlockType: The type of the block
    """
    lines = block.split("\n")
    
    # Check for heading: starts with 1-6 # followed by space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    # Check for code block: starts and ends with 3 backticks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for quote block: every line must start with ">" (with or without space after)
    if all(line.startswith("> ") or line == ">" for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered list: every line must start with "- "
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list: every line must start with number. and space
    # Numbers must start at 1 and increment by 1
    is_ordered_list = True
    for i, line in enumerate(lines):
        expected_number = i + 1
        if not re.match(rf"^{expected_number}\. ", line):
            is_ordered_list = False
            break
    
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    # Default to paragraph
    return BlockType.PARAGRAPH
