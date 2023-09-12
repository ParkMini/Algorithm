N = int(input())
score = list(map(int, input().split()))
M = max(score)
newAvg = sum([(score/M)*100 for score in score]) / N
print(newAvg)