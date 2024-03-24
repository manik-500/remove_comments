import os
import re

def remove_comments_and_docstrings(folder_path):
    """
    Remove comments and docstrings from all .py files in the given folder.

    Args:
    - folder_path (str): Path to the folder containing .py files.

    Returns:
    - None
    """
    # Regular expression pattern to match comments and docstrings
    pattern = re.compile(r'(\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\"|#[^\n]*$)', re.MULTILINE)
    
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.py') or filename.endswith('.yaml'):
            filepath = os.path.join(folder_path, filename)
            
            # Read the content of the file
            with open(filepath, 'r') as file:
                content = file.read()
            
            # Remove comments and docstrings
            cleaned_content = re.sub(pattern, '', content)
            
            # Write the cleaned content back to the file
            with open(filepath, 'w') as file:
                file.write(cleaned_content)

    print(f"Comments and docstrings removed from .py files in {folder_path}")

if __name__ == "__main__":
    folder_path = './example_folder'
    remove_comments_and_docstrings(folder_path)
