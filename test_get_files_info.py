from functions.get_files_info import get_files_info 


def main():
    result_current = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(f"  {result_current}")

    result_pkg = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(f"  {result_pkg}")

    result_bin = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(f"  {result_bin}")

    result_up = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(f"  {result_up}")

if __name__ == "__main__":
    main()
