import os

def write_file(working_directory, file_path, content):
  retstring = ""
  my_file = os.path.join(working_directory, file_path)
  abs_my_file = os.path.abspath(my_file)
  if abs_my_file.startswith(os.path.abspath(working_directory)):
    try:
      with open(my_file, "w") as f:
        f.write(content)
      except PermissionError:
        return(f"Error: You do not have permission to access '{my_file}'.")
      except Exception as e:
        return(f"Error: An unexpected error occurred: {e}")
    return retstring + oversize
  else:
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
