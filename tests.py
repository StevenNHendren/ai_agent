from functions.get_file_content import get_file_content

def main():
  retstring = get_file_content("calculator", "main.py") + "\n"
  retstring += get_file_content("calculator", "pkg/calculator.py") + "\n"
  retstring += get_file_content("calculator", "/bin/cat") + "\n"
  retstring += get_file_content("calculator", "pkg/does_not_exist.py") + "\n"
  print(retstring)

main()
