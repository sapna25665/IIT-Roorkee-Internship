# Search for a keyword in a file

keyword = input("Enter keyword: ")

with open("sample.txt", "r") as file:
    print("\nMatching Lines:")

    for line in file:
        if keyword.lower() in line.lower():
            print(line.strip())
