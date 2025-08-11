import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
  abs_p_wd = os.path.abspath(working_directory)
  my_dir = os.path.join(working_directory, directory)
  abs_p_d = os.path.abspath(my_dir)
  if abs_p_d.startswith(abs_p_wd):
    if os.path.exists(my_dir):
      if file_path.endswith(".py"):
        try:
          pass
        catch Exception as e:
          return f"Error: executing Python file: {e}"
      else:
        return f'Error: "{file_path}" is not a Python file.'  
    else:
      return f'Error: File "{file_path}" not found.'
  else:
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

      




