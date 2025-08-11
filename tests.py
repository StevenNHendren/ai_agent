from functions.get_file_content import get_file_content

def main():
  retstring = get_file_content("calculator", "main.py")
  retstring += get_file_content("calculator", "pkg/calculator.py")
  retstring += get_file_content("calculator", "/bin/cat")
  retstring += get_file_content("calculator", "pkg/does_not_exist.py")
  print(retstring)

main()
