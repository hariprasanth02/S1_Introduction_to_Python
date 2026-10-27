n=int(input("Enter the number of questions:"))

student_ans = []
correct_ans = []

for i in range(n):
    answer = input(f"Question {i+1}:")
    student_ans.append(answer)


for i in range(n):
    answer=input(f"Answer {i+1}:")
    correct_ans.append(answer)

score = 0

for given,correct in zip(student_ans,correct_ans):
    if given == correct:
        score+= 1

print(f"Score :{score}/{n}")
