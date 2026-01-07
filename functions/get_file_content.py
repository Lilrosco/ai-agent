import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_content_string = None

        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            # After reading the first MAX_CHARS if more characters exist add truncated message
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string            
    except OSError as ose:
        return f"Error: Problem with file - {file_path} -> {ose}"
    except Exception as e:
        return f"Error: {e}"
