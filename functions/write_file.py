import os
from google import genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Runs the specified Python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file (path) to which to write the content, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the specified file.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
  retstring = ""
  bytes_written = 0
  my_file = os.path.join(working_directory, file_path)
  abs_my_file = os.path.abspath(my_file)
  if abs_my_file.startswith(os.path.abspath(working_directory)):
    try:
      with open(my_file, "w") as f:
        bytes_written = f.write(content)
    except PermissionError:
      return(f"Error: You do not have permission to access '{my_file}'.")
    except Exception as e:
      return(f"Error: An unexpected error occurred: {e}")
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 
  else:
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
