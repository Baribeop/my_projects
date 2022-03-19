# question 10
score_1 = float (input("Enter first score: "))
score_2 = float (input("Enter second score: "))
score_3 = float (input("Enter third score: "))
score_4 = float (input("Enter fourth score: "))
score_5 = float (input("Enter fith score: "))
score_6 = float (input("Enter sixth score: "))
score_7 = float (input("Enter seventh score: "))
score_8 = float (input("Enter eight score: "))
score_9 = float (input("Enter ninth score: "))
score_10 = float (input("Enter tenth score: "))
scores = [score_1,score_2,score_3,score_4,score_5,score_6,score_7,score_8,score_9,score_10]
print(scores)
p = max(scores)
print(f"The highest score is {p}")
q = min(scores)
print(f"The lowest score is {q}")
value_count = (len(scores))
b = 0
for i in scores:
    b = i + b
    ave_score = (b/value_count) 
print(f"The average score is {ave_score} ")
scores.sort()
print(scores)
print(scores[-2])
for i in scores:
    if i > 100:
        print("A value over 100 has been entered!")
        
scores.pop(0)
scores.pop(1)
value_count1 = len(scores)
d = 0
for i in scores:
    d = i + d
    ave_score1 = (d/value_count1)
print(f"The average of the scores without the two lowest scores is {ave_score1}")
    



