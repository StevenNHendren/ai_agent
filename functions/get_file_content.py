import os

def get_file_content(working_directory, file_path):
  retstring = ""
  my_file = os.path.join(working_directory, file_path)

  if abs_p_d.startswith(os.path.abspath(my_dir)):
    if os.path.isfile(my_file):
      MAX_CHARS = 10000
      with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    else:
      return f'Error: File not found or is not a regular file: "{file_path}"'
  else:
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
