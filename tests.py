from functions.get_file_content import get_file_content

def main():
  retstring = get_file_content("calculator", "lorem.txt")
  
  print(retstring)

main()
