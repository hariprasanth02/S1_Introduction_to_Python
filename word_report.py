counts = {}

with open("text.txt","r") as file:
    text = file.read().lower()

for ch in ".,?":
    text = text.replace(ch,"")

words = text.split()

for word in words:
    counts[word] = counts.get(word,0)+1

with open("report.txt","w") as report:
    report.write(f"Words: {len(words)}\n")
    report.write(f"Unique:{len(counts)}\n\n")

    for word in sorted(counts):
        report.write(f"{word:<10} {counts[word]}\n")

print("Report saved to report.txt")
