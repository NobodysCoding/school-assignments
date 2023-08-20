def main():
    filename = input("Enter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return
    
    num_lines = len(lines)
    
    while True:
        print(f"\nNumber of lines in the file: {num_lines}")
        line_number = int(input("Enter a line number (0 to quit): "))
        
        if line_number == 0:
            print("Goodbye!")
            break
        elif 1 <= line_number <= num_lines:
            print(f"Line {line_number}: {lines[line_number - 1].strip()}")
        else:
            print("Invalid line number. Please enter a number between 1 and", num_lines)

if __name__ == "__main__":
    main()
