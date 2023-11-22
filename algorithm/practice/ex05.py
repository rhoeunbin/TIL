# 예제 05. [오류 해결] 숫자의 길이 구하기

### 오류 코드
number = 22020718
print(len(number))

#오류 이유 : TypeError - int는 len() 함수를 가지고 있지 않음
# ->str로 type을 바꿔줌

number = 22020718
print(len(str(number)))
