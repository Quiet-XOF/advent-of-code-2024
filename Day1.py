# Part 1
with open("Day1-input.txt", "r") as file:
    lines = file.read()

lines = lines.split("\n")
lines1 = []
lines2 = []

for line in lines:
    breakup = line.split()
    if breakup:
        lines1.append(int(breakup[0]))
        lines2.append(int(breakup[1]))

lines1 = sorted(lines1)
lines2 = sorted(lines2)

distance = 0

for i in range(0, len(lines)):
    if lines[i]:
        distance += abs(lines1[i] - lines2[i])

print(f"Distance: {distance}")

# Part 2
similarity = 0

for line1 in lines1:
    count = 0
    for line2 in lines2:
        if line1 == line2:
            count += 1
    similarity += line1 * count

print(f"Similarity: {similarity}")
