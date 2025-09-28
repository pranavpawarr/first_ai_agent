from functions.get_file_content import get_file_content


def test():
    # Test 1: Valid file in calculator directory
    result = get_file_content("calculator", "main.py")
    print('get_file_content("calculator", "main.py"):')
    print(result)
    print("")

    # Test 2: Valid file in subdirectory
    result = get_file_content("calculator", "pkg/calculator.py")
    print('get_file_content("calculator", "pkg/calculator.py"):')
    print(result)
    print("")

    # Test 3: Absolute path outside working directory (should fail)
    result = get_file_content("calculator", "/bin/cat")
    print('get_file_content("calculator", "/bin/cat"):')
    print(result)
    print("")

    # Test 4: Non-existent file (should fail)
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    print(result)
    print("")

if __name__ == "__main__":
    test()
