import csv

# Read student marks
with open("marks.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    results = []

    for row in reader:
        name = row[0]
        marks = list(map(int, row[1:]))

        average = sum(marks) / len(marks)
        results.append([name, average])

# Write results to new CSV file
with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Average"])
    writer.writerows(results)

print("Results saved to results.csv")
