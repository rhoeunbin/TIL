import sys

input = sys.stdin.readline

n = int(input())
first_value = 0

while True:
    first_value += 1
    if "666" in str(first_value):
        list.append(first_value)
    if len(first_value) == n:
        break


#
t = int(input())

li = []

for i in range(2667000):
    six = str(i)
    if '666' in six:
        li.append(six)
        if len(li) == t:
            break
print(li[t-1])