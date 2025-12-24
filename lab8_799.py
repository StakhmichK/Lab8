input_file = "data/input_799_3.txt"
output_file = "data/output_799_3.txt"

participants = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        name = parts[0] + " " + parts[1]
        score = int(parts[-1])
        participants.append((name, score))

max_score = max(p[1] for p in participants)
winners = [p[0] for p in participants if p[1] == max_score]

with open(output_file, "w", encoding="utf-8") as f:
    if len(winners) == 1:
        f.write(winners[0])
    else:
        f.write(str(len(winners)))