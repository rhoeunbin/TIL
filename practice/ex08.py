word = "HappyHacking"

count = 0

for char in word:
    #if char == "a" or "e" or "i" or "o" or "u":
    #오류 이유 : or은 둘 중에 하나만 참이어도 1이 나오므로 모든 알파벳의 개수를 세게 된다.
#각각의 값에 char을 넣어야 모음만 구할 수 있다.
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
        count += 1

print(count)