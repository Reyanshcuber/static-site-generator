from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        # If the node is not a PLAIN type, add it as-is
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        
        # Split the text by the delimiter
        parts = old_node.text.split(delimiter)
        
        # Check if we have an even number of parts (meaning all delimiters are paired)
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: unclosed delimiter '{delimiter}'")
        
        # Process the split parts
        for i, part in enumerate(parts):
            if part == "":
                continue
            
            # Every odd index (1, 3, 5, ...) contains the delimited text
            if i % 2 == 1:
                new_nodes.append(TextNode(part, text_type))
            else:
                new_nodes.append(TextNode(part, TextType.PLAIN))
    
    return new_nodes
    