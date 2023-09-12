dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
print(sum(dial.index(j) + 3 for i in input() for j in dial if i in j))