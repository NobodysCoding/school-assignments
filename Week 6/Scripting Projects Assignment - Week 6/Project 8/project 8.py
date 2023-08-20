def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            data = source.read()
        
        with open(destination_file, 'w') as destination:
            destination.write(data)

        print(f"Contents of '{source_file}' successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print("File not found. Please check the file names and paths.")

if __name__ == "__main__":
    source_file_name = input("Enter the name of the source file: ")
    destination_file_name = input("Enter the name of the destination file: ")

    copy_file(source_file_name, destination_file_name)
