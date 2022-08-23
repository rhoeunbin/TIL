import sys
input = sys.stdin.readline

sen = input().rstrip()



#
import sys

input = sys.stdin.read

alpha = [0] * 26
sentence = input().replace("\n", "").replace(" ", "")

for s in sentence:
    if s.isalpha():
        alpha[ord(s) - 97] += 1
mx = max(alpha)

for i in range(26):
    if mx == alpha[i]:
        print(chr(i + 97), end="")