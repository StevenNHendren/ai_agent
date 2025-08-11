import os

def get_files_info(working_directory, directory="."):
    retstring = ""
    abs_p_wd = os.path.abspath(working_directory)
    #print(abs_p_wd)
    my_dir = os.path.join(working_directory, directory)
    #print(my_dir)
    abs_p_d = os.path.abspath(my_dir)
    if abs_p_d.startswith(abs_p_wd):
        my_dir = os.path.join(working_directory, directory)
        if os.path.exists(my_dir):
            if os.path.isdir(my_dir):
                items = os.listdir(my_dir)
                if len(items) > 0:
                    retstring = "Result for current directory:\n"
                    for item in items:
                        # print(item)
                        try:
                            is_dir = os.path.isdir(os.path.join(my_dir, item))
                            print(is_dir)
                            fs = os.path.getsize(os.path.join(my_dir, item))
                            print(fs)
                            fn= str(item)
                            print(fn)                            
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

