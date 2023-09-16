n = int(input())

arr = [1] * 10
res = 0

for i in range (2, n+1):
    for j in range (1, 10):
        arr[j] = arr[j-1] + arr[j]
for i in range (10):
    res += arr[i]
print(res%10007)