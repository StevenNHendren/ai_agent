import os
import subprocess
from google import genai
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified Python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file (path), relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.LIST,
                default = None,
                description="The arguments to pass to the Python file.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
  abs_p_wd = os.path.abspath(working_directory)
  my_file = os.path.join(working_directory, file_path)
  abs_p_f = os.path.abspath(my_file)
  ret_str = ""
  if abs_p_f.startswith(abs_p_wd):
    if os.path.exists(my_file):
      if file_path.endswith(".py"):
        try:
          command = ["python", file_path]
          command.extend(args)
          my_cpo = subprocess.run(command, capture_output=True, cwd=abs_p_wd, timeout=30)
          if my_cpo.stdout == None:
            ret_str = "No output produced."
          else:
            ret_str += f"STDOUT: {my_cpo.stdout}\n"
          ret_str += f"STDERR: {my_cpo.stderr}\n"
          icode = my_cpo.returncode
          if icode != 0:
            ret_str += f"Process exited with code {icode}\n"
          return ret_str
        except Exception as e:
          return f"Error: executing Python file: {e}"
      else:
        return f'Error: "{file_path}" is not a Python file.'  
    else:
      return f'Error: File "{file_path}" not found.'
  else:
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

      




