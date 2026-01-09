import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    """
    Generate an HTML page from a markdown file using a template.
    
    Args:
        from_path: Path to the markdown file to convert
        template_path: Path to the HTML template file
        dest_path: Path where the generated HTML file should be written
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read template file
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title from markdown
    title = extract_title(markdown_content)
    
    # Replace placeholders in template
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)
    
    # Create destination directory if it doesn't exist
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Write the generated HTML to destination
    with open(dest_path, 'w') as f:
        f.write(full_html)
    
    print(f"Page generated successfully at {dest_path}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generate HTML pages from markdown files in a directory.
    
    Args:
        dir_path_content: Path to the content directory to crawl
        template_path: Path to the HTML template file
        dest_dir_path: Path to the destination public directory
    """
    # List all items in the content directory
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        
        if os.path.isfile(item_path):
            # If it's a markdown file, generate an HTML page
            if item.endswith('.md'):
                # Replace .md with .html for the destination
                dest_file = item.replace('.md', '.html')
                dest_path = os.path.join(dest_dir_path, dest_file)
                generate_page(item_path, template_path, dest_path)
        
        elif os.path.isdir(item_path):
            # If it's a directory, create the same directory in public and recurse
            new_dest_dir = os.path.join(dest_dir_path, item)
            if not os.path.exists(new_dest_dir):
                os.makedirs(new_dest_dir)
            generate_pages_recursive(item_path, template_path, new_dest_dir)

