matches = open("2/data2.txt", "r").read()
data = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
t = [[data[x] for x in l.split()] for l in matches.split("\n")]

score=0
for i, j in t:
    i+1-j


print("Part 1:", sum(b+1 + ((b+1-a)%3)*3 for a, b in t))


print(score)