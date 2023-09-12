for _ in range(int(input())):
    r, s = input().split()
    print("".join(char * int(r) for char in s))