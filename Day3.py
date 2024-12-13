import re

with open("Day3-input.txt", "r") as file:
    lines = file.read()

# Search for mul(number, number)
pattern = r"(mul\((\d+),\s*(\d+)\))|(do\(\))|(don't\(\))"
matches = re.finditer(pattern, lines)

#tasks = [[int(match[0]), int(match[1])] for match in matches]
tasks = []

for match in matches:
    # Get first and second number from mul()
    if match.group(2) and match.group(3): 
        tasks.append([int(match.group(2)), int(match.group(3))])
    # Collect do() and don't()
    elif match.group(4):
        tasks.append(match.group(4))
    elif match.group(5):
        tasks.append(match.group(5))

result = 0
allowed = True

for task in tasks:
    if task == "do()":
        allowed = True
    elif task == "don't()":
        allowed = False
    if allowed and len(task) == 2:
        result += int(task[0]) * int(task[1])
    
print("Results:", result)