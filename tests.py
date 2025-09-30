from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def test():
    # Test 1: "read the contents of main.py" -> get_file_content({'file_path': 'main.py'})
    result = get_file_content(".", "main.py")
    print('get_file_content({"file_path": "main.py"}):')
    print(result)
    print("")
    
    # Test 2: "write 'hello' to main.txt" -> write_file({'file_path': 'main.txt', 'content': 'hello'})
    result = write_file(".", "main.txt", "hello")
    print('write_file({"file_path": "main.txt", "content": "hello"}):')
    print(result)
    print("")
    
    # Test 3: "run main.py" -> run_python_file({'file_path': 'main.py'})
    result = run_python_file(".", "main.py")
    print('run_python_file({"file_path": "main.py"}):')
    print(result)
    print("")
    
    # Test 4: "list the contents of the pkg directory" -> get_files_info({'directory': 'pkg'})
    result = get_files_info(".", "pkg")
    print('get_files_info({"directory": "pkg"}):')
    print(result)
    print("")

if __name__ == "__main__":
    test()
