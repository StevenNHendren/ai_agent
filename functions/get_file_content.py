import os
from config import *

def get_file_content(working_directory, file_path):
  retstring = ""
  my_file = os.path.join(working_directory, file_path)
  oversize = ""
  if abs_p_d.startswith(os.path.abspath(my_dir)):
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
