from pathlib import Path

full_path = Path("D:/Tutedude Assignments/Tutedude_Assignment4/sample.txt")
file_name = full_path.name
try:
    with open("sample2.txt","rt") as fh:
        print("Reading file content: ")
        count = 1
        for line in fh:
            print(f"Line {count}: {line}")
            count = count + 1

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")


