words = list(map(int, input().split()))
print(words)
#오류이유: 문자열인데 int 사용해 숫자로 전환함
words = list(map(str, input().split()))
print(words)