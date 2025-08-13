import os
from functions.config import *
from google import genai
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Returns the content of the specified file, truncated at 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
  retstring = ""
  my_file = os.path.join(working_directory, file_path)
  oversize = ""
  abs_my_file = os.path.abspath(my_file)
  if abs_my_file.startswith(os.path.abspath(working_directory)):
    if os.path.isfile(my_file):
      if (os.path.getsize(my_file) > MAX_CHARS):
        oversize = f'[[...File "{file_path}" truncated at 10000 characters]]'
      try:
        with open(my_file, "r") as f:
          retstring = f.read(MAX_CHARS)
      except FileNotFoundError:
        return(f"Error: The file '{my_file}' was not found.")
      except PermissionError:
        return(f"Error: You do not have permission to access '{my_file}'.")
      except Exception as e:
        return(f"Error: An unexpected error occurred: {e}")
      return retstring + oversize
    else:
      return f'Error: File not found or is not a regular file: "{file_path}"'
  else:
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
