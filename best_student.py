n=int(input("Enter the number of students:"))
scores = []

for i in range(n):
    score=int(input(f"Enter score of students {i+1}:"))
    scores.append(score)

best = -1
starting_pos = 0

for position,score in enumerate(scores,start=1):
    if score > best:
        best = score
        starting_pos = position

print(f"Best :{best} (student #{starting_pos}) ")