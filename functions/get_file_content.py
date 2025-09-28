import os 
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    working_dir = os.path.abspath(working_directory)
    file_p = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_p.startswith(working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_p):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_p, "r") as f:
            content = f.read()
            if len(content) > MAX_CHARS:
                content = content[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    except Exception as e:
        return f"Error: {e}"
