import os

def get_files_info(working_directory, directory="."):

    if os.path.isdir(os.path.getpath(directory):
        abs_p_wd = os.path.abspath(working_directory)
        abs_p_d = os.path.abspath(direcotry)
        if abs_p_wd == os.path.commonpath([abs_p_wd, abs_p_d]):
            my_dir = os.path.join(working_directory, diretory)
            if os.path.exists(my_dir):
                items = os.listdir(my_dir)
                if len(items) > 0:
                    retstring = "Result for current directory:/n"
 - main.py: file_size=576 bytes, is_dir=False
 - tests.py: file_size=1343 bytes, is_dir=False
 - pkg: file_size=92 bytes, is_dir=True
                    for item in items:
                        if os.path.isfile(item):
                            try:
                                fs = os.path.getsize(item)
                                fn= str(item)
                                retstring += f" - {fn}: file_size={fs} bytes, is_dir=False"
                            except OSError:
                                return f"Error: cannot get {item) size"
                        elif os.path.isdir(item):
                            try:
                                fs = os.path.getsize(item)
                                fn= str(item)
                                retstring += f" - {fn}: file_size={fs} bytes, is_dir=True"
                            except OSError:
                                return f"Error: cannot get {item) size"
                else:
                    return f"Error: no items found in {directory}"
            else:
                f'Error: "{directory}" does not exist'
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        return f'Error: "{directory}" is not a directory'

