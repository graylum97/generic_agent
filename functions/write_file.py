import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes (or overwrites) a text file at the specified path (creates parent dirs if needed) and returns success with character count or error",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write (or overwrite) to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The data that will be written to the specified file",
            ),
        },
        required=["file_path", "content"]
    ),
)
