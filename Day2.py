# Part 1
with open("Day2-input.txt", "r") as file:
    lines = file.read()

lines = lines.split("\n")
reports = []

for line in lines:
    breakup = line.split()
    if breakup:
        reports.append([int(num) for num in breakup])

safe_reports = 0

def check1(report): # Either increase or decrease
    sorted_report = sorted(report)
    if sorted_report == report:
        return True
    reverse_report = sorted_report[::-1]
    if reverse_report == report:
        return True
    return False

def check2(report): # Ints differ by at least one, at most three
    for i in range(0, len(report) - 1):
        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

for report in reports:
    if check1(report) == True and check2(report) == True:
        safe_reports += 1

print(f"Safe Reports: {safe_reports}")

# Part 2