import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(os.path.normpath(working_directory))
        abs_file_path = os.path.abspath(os.path.normpath(os.path.join(working_dir_abs, file_path)))
        common = os.path.commonpath([working_dir_abs, abs_file_path])

        if common != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}"as it is a directory'

        parent_dir = os.path.dirname(abs_file_path)
        os.makedirs(parent_dir, exist_ok=True)

        with open(abs_file_path, "w") as f:
            f.write(content)

        return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

    except Exception as e:
        return f"Error: writing to file: {e}"
