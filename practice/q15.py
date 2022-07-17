# #15번
# 문자열 word가 주어질 때, 해당 문자열에서 `a` 가 처음으로 등장하는 위치(index)를 출력해주세요.
# `a` 가 없는 경우에는 `-1`을 출력해주세요.
# `**find()` `index()` 메서드 사용 금지**

#word = 'banana'

word=input()
cnt = 0

for i in word : 
    if i == 'a':
        break
    cnt +=1   #단어에 'a'가 없는 경우도 있을 수 있음
else :
    i = -1   #'a'가 없을 때
print(cnt)