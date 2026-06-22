# Count error types in a log file

error_count = {}

with open("log.txt", "r") as file:
    for line in file:
        error = line.strip()

        if error in error_count:
            error_count[error] += 1
        else:
            error_count[error] = 1

print("Log Analysis:")
for error, count in error_count.items():
    print(error, ":", count)
