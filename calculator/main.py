import sys
from pkg.calculator import Calculator
from pkg.render import render

def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>" [filename]')
        print('Example: python main.py "3 + 5" result.txt')
        return

    expression = " ".join(sys.argv[1:-1]) if len(sys.argv) > 2 else sys.argv[1]
    filename = sys.argv[-1] if len(sys.argv) > 2 else None

    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)

        if filename:
            try:
                default_api.write_file(content=to_print, file_path=filename)
                print(f"Result saved to {filename}")
            except Exception as e:
                print(f"Error saving to file: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
