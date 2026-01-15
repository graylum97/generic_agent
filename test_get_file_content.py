from functions.get_file_content import get_file_content
from config import MAX_FILE_CHARS

def main():
    content = get_file_content("calculator", "lorem.txt")
    print(content)

    assert len(content) >= MAX_FILE_CHARS
    assert content.endswith(f'[...File "lorem.txt" truncated at {MAX_FILE_CHARS} characters]')

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()
