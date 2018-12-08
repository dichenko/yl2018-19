
m = []
with open("input.txt") as f:
    for el in f.readlines():
        m.append(el.strip())
m.sort()
print(m)

