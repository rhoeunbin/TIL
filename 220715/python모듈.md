#### 모듈

- (합, 평균, 표준편차 등) 다양한 기능을 하나의 파일로

- 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성

#### 패키지

- 다양한 파일을 하나의 폴더로(모듈의 집합)

- 패키지 안에 또 다른 서브 패키지를 포함

#### 라이브러리

- 다양한 패키지를 하나의 묶음으로

#### pip

- 이것을 관리하는 관리자

- 파이썬 표준 라이브러리



#### 데이터타임

```python
import datetime #날짜와 시간 조정->오늘부터 100일 지난 뒤 날짜 계산 등,,
#import : 모듈을 가져오기
now= datatime.datatime123.now()
print(now, type(now))

#form datetime.import datetime123
#now=datatime.now()   과 동일
```

```python
import random

numbers = random.sample([1,2,3],2)
print(numbers,type(numbers))
#[1,2] <class 'list'>


#1~45까지의 숫자 그 중에 6개
numbers = random.sample(range(1,46),6)
numbers.sort() #정렬
print(numbers,type(numbers))

n=int(input('얼마쓸래?'))
for i in tange(n):
    numbers = random.sample(range(1,46),6)
    numbers.sort()
    print(numbers)
```

*잘 모를 때는 파이썬 자습서 활용하기*

[파이썬 자습서](https://docs.python.org/ko/3/tutorial/index.html)



JSON 프로젝트 함 - 굉장히 어려웠음,,,ㅠㅜㅠㅜ
