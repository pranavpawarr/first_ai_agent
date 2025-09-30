from functions.run_python_file import run_python_file


def test():
    # Test 1: Valid file showing usage instructions
    result = run_python_file("calculator", "main.py")
    print('run_python_file("calculator", "main.py"):')
    print(result)
    print("")

    # Test 2: Calculator with arguments (expecting nasty rendered result)
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print('run_python_file("calculator", "main.py", ["3 + 5"]):')
    print(result)
    print("")

    # Test 3: Running tests in calculator directory
    result = run_python_file("calculator", "tests.py")
    print('run_python_file("calculator", "tests.py"):')
    print(result)
    print("")

    # Test 4: Invalid path outside working directory (should fail)
    result = run_python_file("calculator", "../main.py")
    print('run_python_file("calculator", "../main.py"):')
    print(result)
    print("")

    # Test 5: Non-existent file (should return error)
    result = run_python_file("calculator", "nonexistent.py")
    print('run_python_file("calculator", "nonexistent.py"):')
    print(result)
    print("")


if __name__ == "__main__":
    test()
