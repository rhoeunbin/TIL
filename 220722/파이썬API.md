JSON(Java Script

자바 스크립트를 파이썬에 맞춰 변한



### API

> 정보 주고 받을 떄 활용(Application Programming Interface : 응용 프로그램 인터페이스) , 
>
> 컴퓨터와 컴퓨터 프로그램 사이의 연결

**주소를 요청하면 문서로 응답해준다**

- 활용시 주의 사항
  - 요청하는 방식에 대한 이해
    - 인증 방식
    - **url 생성**
    - 요청 변수(필수와 선택)
  - 응답 결과에 대한 이해
    - 응답 결과 타입(JSON)



#### API 예시

```python
# pip install requests 
import requests   #import : 모듈 불러오기

# URL로
order_currency = 'BTC' 
payment_currency = 'KRW' 
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

# 요청을 보내고
response = requests.get(URL)   #get() : 딕셔너리 가져오기

# 응답 받은 값을 가져옴
print(response, type(response)) # <Response [200]> <class 'requests.models.Response'>

# 속성 예시
print(response.status_code) # 200 
print(response.text, type(response.text)) # 문자열

# 메서드 예시
# .json() 텍스트 형식의 JSON 파일을 파이썬 데이터 타입으로 변경!
print(response.json(), type(response.json())) #  <class 'dict'>

data = response.json()
# data는 딕셔너리 => key로 접근
print(data.get('data').get('closing_price'))
```



#### requests 모듈

```python
# 랜덤 이름, 나이
# https://api.agify.io?name=michael
import requests

URL = 'https://api.agify.io'
params = {
    'name': 'eunbin'
}
response = requests.get(URL, params=params).json()
print(response)
```

객체는 메소드와 속성으로 이루어짐

responce 객체

get, post - requests.get(가져오기), requests.post(게시)



##### TMDB API 활용예시

>  영화 정보 제공

developers - movie로 들어가서 하기

*중괄호가 없으면 path 그대로*

- 깃헙에 커밋을 최근에 얼마나 했는지 등 알 수 있음

  자피어, ifttt 등이 API 활용한 회사들

  

  **api key 각자 발급 받아서 하기**