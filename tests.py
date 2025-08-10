from functions.get_files_info import get_files_info

def main():
  retstring = get_files_info("calculator", ".")

  retstring += get_files_info("calculator", "pkg")

  retstring += get_files_info("calculator", "/bin")

  retstring += get_files_info("calculator", "../")
  
  print(retstring)

main()
