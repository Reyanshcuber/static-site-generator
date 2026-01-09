from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_images_and_links import split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    """
    Convert raw markdown text into a list of TextNode objects with proper formatting.
    
    Parses bold (**), italic (_), code (`), images (![...](url)), and links ([...](url)).
    """
    # Start with a single plain text node
    nodes = [TextNode(text, TextType.PLAIN)]
    
    # Split by bold delimiter
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    # Split by italic delimiter
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    # Split by code delimiter
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Split by images
    nodes = split_nodes_image(nodes)
    
    # Split by links
    nodes = split_nodes_link(nodes)
    
    return nodes