from pathlib import Path

try:
    content = input("Enter text to write to the file: ")

    full_path = Path("D:/Tutedude Assignments/Tutedude_Assignment4/output.txt")
    file_name = full_path.name

    with open("output.txt", "wt") as fh:
        fh.write(content)

    print(f"Data successfully written to {file_name}.")
    print("\n")

    append_data = input("Enter additional text to append: ")


    with open("output.txt","at") as fh:
        fh.write(append_data)

    print(f"Data successfully appended.")
    print("\n")

    print(f"File content of {file_name}: ")
    print(content)
    print(append_data)

except Exception as err:
    print(err)


