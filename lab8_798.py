input_file = "data/input_798_3.txt"
output_file = "data/output_798_3.txt"

max_scores = {9: -1, 10: -1, 11: -1}
winners = {9: 0, 10: 0, 11: 0}

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.split()
        grade = int(parts[-2])
        score = int(parts[-1])

        if score > max_scores[grade]:
            max_scores[grade] = score
            winners[grade] = 1
        elif score == max_scores[grade]:
            winners[grade] += 1

with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"{winners[9]} {winners[10]} {winners[11]}")