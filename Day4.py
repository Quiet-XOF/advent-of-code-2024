# Part 1
with open("Day4-input.txt", "r") as file:
    lines = file.readlines()
reports = [line.strip() for line in lines]

def check_word(sample):
    return sample == "XMAS" or sample == "SAMX"        

# Horizontal
horizontal_count = 0
for report in reports:
    for i in range(0, len(report[:-3])):
        sample = report[i:i+4]
        if check_word(sample):
            horizontal_count += 1

# Vertical
vertical_count = 0
for i, report in enumerate(reports[:-3]):
    for j in range(0, len(report)):
        sample = reports[i][j] + reports[i+1][j] + reports[i+2][j] + reports[i+3][j]
        if check_word(sample):
            vertical_count += 1

# Diagonal
diagonal_count = 0
for i, report in enumerate(reports[:-3]):
    for j in range(0, len(report[:-3])):
        sample1 = reports[i][j] + reports[i+1][j+1] + reports[i+2][j+2] + reports[i+3][j+3]
        sample2 = reports[i][j+3] + reports[i+1][j+2] + reports[i+2][j+1] + reports[i+3][j]
        if check_word(sample1):
            diagonal_count += 1
        if check_word(sample2):
            diagonal_count += 1

print("Horizontal Count:", horizontal_count)
print("Vertical Count:", vertical_count)
print("Diagonal Count:", diagonal_count)
print("XMAS Count:", horizontal_count + vertical_count + diagonal_count)

# Part 2, actual X-MAS
def check_xmas(sample):
    return sample == "MAS" or sample == "SAM"

xmas_count = 0
for i, report in enumerate(reports[:-2]):
    for j in range(0, len(report[:-2])):
        sample1 = reports[i][j] + reports[i+1][j+1] + reports[i+2][j+2]
        sample2 = reports[i][j+2] + reports[i+1][j+1] + reports[i+2][j]
        if check_xmas(sample1) and check_xmas(sample2):
            xmas_count += 1

print("Actual X-MAS Count:", xmas_count)