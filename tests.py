from functions.run_python import run_python_file

def main():
  retstring = run_python_file("calculator", "main.py") + "\n"
  retstring += run_python_file("calculator", "main.py", ["3 + 5"]) + "\n"
  retstring += run_python_file("calculator", "tests.py") + "\n"
  retstring += run_python_file("calculator", "../main.py") + "\n"
  retstring += run_python_file("calculator", "nonexistent.py") + "\n"
  print(retstring)

main()
