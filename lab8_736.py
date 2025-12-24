input_file = "data/input_736_3.txt"
output_file = "data/output_736_3.txt"
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
with open(output_file, "w", encoding="utf-8") as f:
    for line in reversed(lines):
        f.write(line.rstrip("\n")[::-1] + "\n")