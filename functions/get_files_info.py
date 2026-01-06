import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        with os.scandir(target_dir) as entries:
            dir_info = []

            for entry in entries:
                dir_info.append(f"- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}")
                # print(entry.name)
                # if entry.is_file():
                #     print(f"  {entry.name} is a file")
                # elif entry.is_dir():
                #     print(f"  {entry.name} is a directory")
            return "\n".join(dir_info)
    except Exception as e:
        return f"Error: {e}"
