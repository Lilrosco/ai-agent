import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif target_path[-2:] != "py":
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]

        command.extend(args) if args else None

        process_result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        
        result_str = []

        if process_result.returncode != 0:
            result_str.append("Process exited with code X")
        
        std_err = process_result.stderr
        std_out = process_result.stdout
        
        if not std_out and not std_err:
            result_str.append("No output produced")
        else:
            if std_out:
                result_str.append(f"STDOUT: {std_out}")
            if std_err:
                result_str.append(f"STDERR: {std_err}")
        
        return ". ".join(result_str)
    except Exception as e:
        return f"Error: executing Python file: {e}"
