n = int(input())
stair = [int(input()) for _ in range(n)]
visited = [0] * n

# 각 계단에 대한 최대 점수 계산
for i in range(n):
    if i == 0:
        # 첫 번째 계단의 최대 점수는 그 계단의 점수와 같음
        visited[i] = stair[i]
    elif i == 1:
        # 두 번째 계단의 최대 점수는 첫 번째 계단과 두 번째 계단 중 큰 값
        visited[i] = max(stair[i - 1] + stair[i], stair[i])
    else:
        # 세 번째 계단부터는 두 가지 옵션을 고려하여 최대 점수 계산
        # 1. 현재 계단을 오르고 직전 계단을 밟지 않는 경우
        # 2. 현재 계단을 오르고 직전 계단을 밟는 경우 (두 계단을 건너뛰고 올라감)
        # 이 두 옵션 중에서 더 큰 값을 선택하여 현재 계단까지의 최대 점수를 계산
        visited[i] = max(visited[i - 2], visited[i - 3] + stair[i - 1]) + stair[i]

print(visited[-1])