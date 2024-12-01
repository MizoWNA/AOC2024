raw = open("day1.txt", "r").read()

processed = raw.split()

list1 = processed[::2]
list2 = processed[1::2]

list1 = list(map(int, list1))
list2 = list(map(int, list2))

list1.sort()
list2.sort()

tot = []

for i in range(0, len(list1)):
    tot.append(abs((list1[i]) - list2[i]))

print(sum(tot))