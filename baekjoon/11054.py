n = int(input())
arr = list(map(int, input().split()))
dp1, dp2 = [1] * n, [1] * n
for i in range(n):
    dp1[i] = max((dp1[j]+1 for j in range(i) if arr[i]>arr[j]), default=1)
for i in range(n - 1, -1, -1):
    dp2[i] = max((dp2[j]+1 for j in range(n-1,i,-1) if arr[i]>arr[j]), default=1)
print(max(dp+dp2-1 for dp, dp2 in zip(dp1, dp2)))