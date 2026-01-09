import os
import sys
import shutil
from generate_page import generate_pages_recursive

def copy_files_recursive(source_dir, dest_dir):
    """
    Recursively copy all files and directories from source_dir to dest_dir.
    First deletes all contents of destination directory.
    """
    # Delete destination directory if it exists
    if os.path.exists(dest_dir):
        print(f"Deleting {dest_dir}")
        shutil.rmtree(dest_dir)
    
    # Create destination directory
    os.mkdir(dest_dir)
    print(f"Created {dest_dir}")
    
    # Copy all files and subdirectories
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isfile(source_path):
            # Copy file
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} -> {dest_path}")
        else:
            # Recursively copy directory
            copy_files_recursive(source_path, dest_path)

def main():
    # Get the root directory (where the script is run from)
    root_dir = os.path.dirname(__file__)
    
    # Get basepath from CLI argument, default to /
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    print(f"Building site with basepath: {basepath}")
    
    # Copy static files to docs directory
    static_source = os.path.join(root_dir, "..", "static")
    docs_dest = os.path.join(root_dir, "..", "docs")
    
    print("=== Copying static files ===")
    copy_files_recursive(static_source, docs_dest)
    
    # Generate pages recursively from all markdown files in content directory
    print("\n=== Generating pages ===")
    content_dir = os.path.join(root_dir, "..", "content")
    template_path = os.path.join(root_dir, "..", "template.html")
    docs_dir = os.path.join(root_dir, "..", "docs")
    
    generate_pages_recursive(content_dir, template_path, docs_dir, basepath)
    
    print("\n=== Static site generation complete! ===")

if __name__ == "__main__":
    main()