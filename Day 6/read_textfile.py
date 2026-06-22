# Read a text file and count lines, words, and characters

file_name = "sample.txt"

with open(file_name, "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)
