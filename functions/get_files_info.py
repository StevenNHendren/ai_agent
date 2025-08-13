import os
import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
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

def get_files_info(working_directory, directory="."):
    retstring = ""
    abs_p_wd = os.path.abspath(working_directory)

    my_dir = os.path.join(working_directory, directory)

    abs_p_d = os.path.abspath(my_dir)
    if abs_p_d.startswith(abs_p_wd):
        my_dir = os.path.join(working_directory, directory)
        if os.path.exists(my_dir):
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
        else:
            f'Error: "{directory}" does not exist\n'
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

    return retstring

