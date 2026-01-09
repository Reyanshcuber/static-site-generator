from textnode import TextType, TextNode
from extract_markdown_images_and_links import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    
    for old_node in old_nodes:
        # If the node is not a PLAIN type, add it as-is
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        
        # Extract images from the text
        images = extract_markdown_images(old_node.text)
        
        # If no images found, add the node as-is
        if not images:
            new_nodes.append(old_node)
            continue
        
        # Split the text by images
        current_text = old_node.text
        for alt_text, url in images:
            # Find the image markdown pattern and split
            image_pattern = f"![{alt_text}]({url})"
            parts = current_text.split(image_pattern, 1)
            
            # Add the text before the image (if any)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.PLAIN))
            
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # Continue with the remaining text
            current_text = parts[1] if len(parts) > 1 else ""
        
        # Add any remaining text
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.PLAIN))
    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    
    for old_node in old_nodes:
        # If the node is not a PLAIN type, add it as-is
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        
        # Extract links from the text
        links = extract_markdown_links(old_node.text)
        
        # If no links found, add the node as-is
        if not links:
            new_nodes.append(old_node)
            continue
        
        # Split the text by links
        current_text = old_node.text
        for link_text, url in links:
            # Find the link markdown pattern and split
            link_pattern = f"[{link_text}]({url})"
            parts = current_text.split(link_pattern, 1)
            
            # Add the text before the link (if any)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.PLAIN))
            
            # Add the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            
            # Continue with the remaining text
            current_text = parts[1] if len(parts) > 1 else ""
        
        # Add any remaining text
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.PLAIN))
    
    return new_nodes

