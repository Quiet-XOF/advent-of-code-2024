with open("Day2-input.txt", "r") as file:
    lines = file.readlines()

reports = [list(map(int, line.strip().split())) for line in lines]

safe_reports = 0
damp_reports = 0

def safe_list(report):
    # Check ascending and descending
    # Check if difference is at least 1 and at most 3
    return sorted(report) in [report, report[::-1]] \
    and all(1 <= abs(first-second) <= 3 for first, second in zip(report, report[1:]))

for report in reports:
    if safe_list(report):
        safe_reports += 1
    # Slice the list and see if the left and right side can pass at least once
    elif any(safe_list(report[:i] + report[i+1:]) for i in range(len(report))):
        damp_reports += 1

print("Safe reports:", safe_reports)
print("With dampening:", safe_reports + damp_reports)