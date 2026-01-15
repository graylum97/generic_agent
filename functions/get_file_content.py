import os
from config import MAX_FILE_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(os.path.normpath(working_directory))
        abs_file_path = os.path.abspath(os.path.normpath(os.path.join(working_dir_abs, file_path)))
        common = os.path.commonpath([working_dir_abs, abs_file_path])

        if common != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path, "r") as f:
            content = f.read(MAX_FILE_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_FILE_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"
