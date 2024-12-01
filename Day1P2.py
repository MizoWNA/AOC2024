raw = open("day1.txt", "r").read()

processed = raw.split()

list1 = processed[::2]
list2 = processed[1::2]

list1 = list(map(int, list1))
list2 = list(map(int, list2))

list1.sort()
list2.sort()

counts = []

for num in list1:
    counts.append(list2.count(num))

similarity = 0

for i in range(len(list1)):
    similarity = similarity + (counts[i] * list1[i])

print(similarity)