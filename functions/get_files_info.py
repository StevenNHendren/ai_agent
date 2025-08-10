import os

def get_files_info(working_directory, directory="."):
    retstring = ""
    abs_p_wd = os.path.abspath(working_directory)
    abs_p_d = os.path.abspath(directory)
    if abs_p_d.startswith(abs_p_wd):
        my_dir = os.path.join(working_directory, diretory)
        if os.path.exists(my_dir):
            if os.path.isdir(mydir):
                items = os.listdir(my_dir)
                if len(items) > 0:
                    retstring = "Result for current directory:\n"
                    for item in items:
                        if os.path.isfile(item):
                            try:
                                fs = os.path.getsize(item)
                                fn= str(item)
                                retstring += f" - {fn}: file_size={fs} bytes, is_dir=False\n"
                            except OSError:
                                return f"Error: cannot get {item} size\n"
                        elif os.path.isdir(item):
                            try:
                                fs = os.path.getsize(item)
                                fn= str(item)
                                retstring += f" - {fn}: file_size={fs} bytes, is_dir=True\n"
                            except OSError:
                                return f"Error: cannot get {item} size\n"
                else:
                    return f"Error: no items found in {directory}\n"
            else:
                return f'Error: "{directory}" is not a directory\n'        
        else:
            f'Error: "{directory}" does not exist\n'
    else:
        eturn f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

    return retsrring

