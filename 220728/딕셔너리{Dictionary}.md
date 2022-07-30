### 딕셔너리{Dictionary}

> 해시 테이블



- key-value
- 순서가 없다
- key는 immutable(변경 불가능)



해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 메핑

해시 : 해시 함수를 통해 얻어진 값

해시 함수와 해시 테이블을 이용하기 떄문에

**삽입, 삭제, 수정, 조회연산의 속도가 리스트보다 빠름**



중간에 넣으면 복잡도가 올라감 (insert - O(n) or O(1)= 끝자리에 추가할 떄)



🙄**딕셔너리는 언제 사용..?**

1. 리스트 사용하기 힘들 때
2. 데이터에 대한 빠른 접근 탐색이 필요할 때
3. 현실 세계의 대부분의 데이터를 다룰 경우



### 📝딕셔너리 기본 문법 정리

- 선언 
  - 변수 = {key1:value1, key2:value2}
- 삽입/수정
  - 딕셔너리[key]=
- 삭제
  - 딕셔너리.pop(key, default)
- 조회 
  - 딕셔너리[key]
  - 딕셔너리.get(key,default)



`{}` 내부에 키가 없으면 삽입, 있으면 변경

`.pop ` : 내부에 존재하는 key에 대한 value삭제 및 반환

key가 없다면 None 반환





✔✔*딕셔너리 조회 차이 확인*

```python
a = {
    'name':'bin'
    'gender':'male'
    'address':'seoul'
}
print(a['name'])  #bin
print(a.get('name'))  #bin

print(a['phone'])  #KeyError : phone
print(a.get('phone')  #None
print(a.get('phone','없음')) #없음
```



```python
john = {
    "name" : "john"
    "role" : "ceo"
}

print(john)  #key값들 나옴
print(john[elen]) #value 값이 print 됨

print(john.keys) 
```



### 딕셔너리 메서드

`.keys` key들의 데이터가 나옴  <class> dict_keys

`.values`  value들의 데이터 나옴

`.items`  key와 value가 같이 나옴 =>튜플이 나옴(key-value 페어들이 나옴)



from collections import Counter

print(Counter(user_input))



print(dir(Counter(user_input))) 하면 흑마법

