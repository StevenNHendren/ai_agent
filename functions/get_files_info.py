import os

def get_files_info(working_directory, directory="."):

    if os.path.isdir(os.path.getpath(directory):
        abs_p_wd = os.path.abspath(working_directory)
        abs_p_d = os.path.abspath(direcotry)
        if abs_p_wd == os.path.commonpath([abs_p_wd, abs_p_d]):
            pass
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        return f'Error: "{directory}" is not a directory'
    if os.path.exists(absolute_path):
        pass
    else:
        f'Error: "{directory}" does not exist'
