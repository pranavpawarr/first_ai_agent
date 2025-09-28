from functions.write_file import write_file

def test():
    # Test 1: Valid file in calculator directory
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):')
    print(result)
    print("")

    # Test 2: Valid file in subdirectory
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):')
    print(result)
    print("")

    # Test 3: Absolute path outside working directory (should fail)
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):')
    print(result)
    print("")

if __name__ == "__main__":
    test()
