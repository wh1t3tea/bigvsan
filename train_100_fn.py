with open("LibriTTS/train-full.txt", "r") as f:
    lines = f.readlines()
    valid_rows = []
    for line in lines:
        if line.split("/")[0] == "train-clean-100":
            valid_rows.append(line)
with open("LibriTTS/train-clean-100.txt", "w") as d:
    d.write("".join(valid_rows))
    d.close()