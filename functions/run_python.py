import os

def run_python_file(working_directory, file_path, args=[]):
  abs_p_wd = os.path.abspath(working_directory)
  my_dir = os.path.join(working_directory, directory)
  abs_p_d = os.path.abspath(my_dir)
  if abs_p_d.startswith(abs_p_wd):
    if os.path.exists(my_dir):
      if file_path.endswith(".py"):
        pass
      else:
        return f'Error: "{file_path}" is not a Python file.'  
    else:
      return f'Error: File "{file_path}" not found.'
  else:
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    

    
    

        
            if os.path.isdir(my_dir):
                items = os.listdir(my_dir)
                if len(items) > 0:
                    retstring = "Result for current directory:\n"
                    for item in items:

                        try:
                            is_dir = os.path.isdir(os.path.join(my_dir, item))

                            fs = os.path.getsize(os.path.join(my_dir, item))

                            fn= str(item)
                       
                            retstring += f" - {fn}: file_size={fs} bytes, is_dir={is_dir}\n"
                        except OSError:
                            return f"Error: cannot get {item} size\n"
                else:
                    return f"Error: no items found in {directory}\n"
            else:
                return f'Error: "{directory}" is not a directory\n'        




