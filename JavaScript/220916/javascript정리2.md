*스타일가이드 한 번 확인해보기*



## 변수와 식별자

- 식별자는 변수를 구분할 수 있는 변수명
- 식별자는 반드시 문다, 달러($) 또는 밑줄(_)로 시작
- 대소문자 구분, 클래스면 외에는 모두 소문자로 시작
- 예약어 사용 불가능



- (참고)선언,할당,초기화
- 선언(Declaration)
  - 변수를 생성하는 행위 또는 시점
- 할당(Assignment)
  - 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화(Intialization)
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```javascript
let foo          // 선언
console.log(foo) // undefined

foo = 11         // 할당
console.log(foo) // 11

let bar = 0      // 선언+할당
console.log(bar) // 0
```



### let, const

> ES6부터 도입, 블록 스코프

let(재할당 가능) => 값 변경 가능

const(재할당 불가능) 

=> 둘 다 재선언 불가능

```javascript
let number = 10  //1. 선언 및 초기값 할당
number = 10      //2. 재할당

console.log(number) // 10
---
const number = 10  //1. 선언 및 초기값 할당
number = 10      // 재할당 불가능
```

```javascript
// 둘 다 재선언 불가능
let number = 10
let number = 50 // uncaught syntax error

---
const number = 10    
const number = 50    
```



=> var과의 가장 큰 차이점

- 블록 스코프*(block scope)

  - if, for 함수 등의 `중괄호 내부` (일종의 변수의 범위)

  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능



### var

> 함수 스코프, 사용X

- var로 선언한 변수는 재선언 및 재할당 모두 가능
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- 호이스팅되는 특성 가지고 있음
- `함수 스코프`를 가짐 (함수의 중괄호 내부, 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능)

```javascript
funtion foo() {
    var x = 5
    console.log(x) //5
}
// ReferenceError : x is not defined
console.log(x)
```



### hoisting

- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환
- 자바 스크립트는 모든 선언을 호이스팅함
- var, let, const 모두 호이스팅이 발생하지만, var는 선언과 동시에 발생하여 일시적 사각지대가 존재 X

```javascript
console.log(username)  //undefined로 값을 가지게 된다
var username = '홍길동'

console.log(email) //Uncaught ReferenceError
let email = 'rhoeb21@gmail.com'

console.log(age)  //Uncaught ReferenceError
const age = 25
```





## 데이터 타입

> 크게 원시 타입과 참조 타입으로 분류

원시 타입(primitive type)

- 객체가 아닌 기본 타입
- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사됨



참조 타입(reference type)

- 객체 타입의 자료형
- 변수에 해당 객체의 참조 값이 담김
- 다른 변수에 복사할 때 참조 값이 복사됨



숫자 타입

- 정수, 실수 구분 없는 하나의 숫자 타입
- 부동소수점 형식을 따름
- NaN (Not-A-Number)



문자열 타입

- 텍스트 데이터를 나타냄
- 16비트 유니코드 문자의 집합
- 작은따옴표 또는 큰따옴표 모두 가능
- 템플릿 리터럴(Template Literal)
  - ES6부터 지원
  - 따옴표 대신 backtick(``) 으로 표현



undefined 

- 변수에 값이 없음



null

- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입
- null 타입과 typeof 연산자



## 연산자

할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자 ++, --



대소 비교 연산자

일치 비교 연산자(===)

동등 비교 연산자(==)

논리 연산자

- and : &&
- or : ||
- not : !

삼항 연산자 (Ternary Operator)

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환

```javascript
console.log(true ? 1 : 2) //1
console.log(false ? 1 : 2) //2
```

조건 ? 참 : 거짓

## 조건문

- if, else if, else
  - 조건은 소괄호
  - 실행할 코드는 중괄호 안에 작성
  - 블록 스코프 생성



### if statement

```javascript
const nation = 'Korea'

if (nation === 'Korea') {
    console.log('안녕')
} else if (nation === 'France'){
    console.log('Bomjour')
} else {
    console.log('Hi')
}
```





### switch statement

- 표현식(expression)과 결과값을 이용한 조건문
- 표현식의 결과값과 case문의 오른쪽 값을 비교
- break 및 default문은 `선택적`으로 사용 가능
- break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행

*break문을 만나야 종료가 된다*

```javascript
switch(expression){
    case 'first value':{
        //do something
        [break]
    }
    case 'second value':{
        //do something
        [break] 
    [default: {
     //do something
     }]
}
```



## 반복문

> 블록 스코프 생성

- while
- for
- for..in
  - 주로 객체의 속성들을 순회할 때 사용
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장X
- for...of
  - 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용
    - 반복 가능한 객체의 종류 : Array, Map, Set, String 등



### while 

> 조건문이 참일 때 반복

- 조건은 소괄호 안에, 실행할 코드는 중괄호 안에

```javascript
while (condition) {
    //do something
}
```



### for

> 세미콜론`;`으로 구분되는 세 부분으로 구성

- initialization
  - 최초 반복문 진입 시 1회만 실행
- condition
  - 매 반복 시행 전 평가
- expression
  - 매 반복 시행 이후 평가

```javascript
for (initialization; condition; expression){
    //do something
}
```



### for ... in => 객체 순회 적합

- 객체(object)와 속성(key)들을 순회할 때 사용
- 배열도 순회 가능하지만 권장X
- 실행할 코드 중괄호 안에 작성

```javascript
for (variable in object) {
    //do something
}
---
const capitals = {
    Korea:'Seoul',
    France:'Paris'
}
for (let capital in capitals){
    console.log(capital)
}
```



### for ...of => 배열 순회 적합

- 반복가능한 객체를 순회하면서 값을 꺼낼 때(배열 순회할 때 사용)
- 실행할 코드는 중괄호 작성

```javascript
for (variable of object) {
    //do something
}
---
const fruits = ['딸기','포도','체리']

for (let fruit in fruits){
    fruit = fruit + '!'
    console.log(fruit)
}
```

*for in으로 배열 순회는 가능하지만 for of 로 객체 순회는 오류*



## 함수

> 참조 타입 중 하나로써 function 타입에 속함
>
> **함수 선언식, 함수 표현식으로 정의**



함수의 정의

- 함수의 이름과 함께 정의하는 방식
- 3가지 부분으로 구성
  - 함수의 이름(name)
  - 매개 변수(args)
  - 함수 body(중괄호 내부)

```javascript
function name(args){
    //do something
}
---
function add(num1,num2){
    return num1 + num2
}
add(1,2)
```





### 함수의 표현식(function expression)

- 함수를 표현식 내에서 정의하는 방식

- 함수의 이름을 생략하고 익명 함수로 전환 가능(익명 함수는 함수 표현식에서만 가능)

```javascript
const name = function name(args){
    //do something 함수를 변수에 저장하는 느낌
}
---
const add = function add(num1,num2){
    return num1 + num2
}
add(1,2)
```



- 기본 인자
  - 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능



**매개변수와 인자의 개수 불일치 허용** -> 자바 스크립트는 가능



- Rest Parameter
  - rest parameter를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음(python의 *args와 유사)



- Spread operator
  - spread oprator를 사용하면 배열 인자를 전개하여 전달 가능



- 호이스팅(hoisting) - 함수 선언식
  - 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생
  - 함수 호출 이후에 선언해도 동작

```javascript
add(2,7) // 9
function add (num1, num2){
    return num1 + num2
}
```



- 호이스팅(hoisting) - 함수 표현식
  - 반면 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
  - 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

```javascript
sub(7,2) // Uncaught ReferenceError : Cannot access 'sub' before initialization

const sub = function (num1, num2) {
    return num1 - num2
}
```

*var로 선언하면, 변수가 선언 전에 undefined로 초기화 되어 다른 에러 발생*



## Arrow Function

> 화살표 함수

- 함수를 비교적 간결하게 정의할 수 있는 문법 
- function 키워드 생략 가능 
- 함수의 매개변수가 단 하나 뿐이라면, ‘( )’ 도 생략 가능 
- 함수 몸통이 표현식 하나라면 ‘{ }’과 return도 생략 가능 



```javascript
const arrow1 = function (name) {
  return `hello, ${name}`
}
// 1. function 키워드 삭제
const arrow2 = (name) => { return `hello, ${name}` }
// 2. 매개변수가 1개일 경우에만 ( ) 생략 가능
const arrow3 = name => { return `hello, ${name}` }
// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 { } & return 삭제
가능
const arrow4 = name => `hello, ${name}`
```





## 문자열

> 메서드 => 찾아서 읽어보기

- `string.includes(value) `
  - 문자열에 value가 존재하는지 판별 후 참 또는 거짓 반환
- `string.split(value) `
  - value가 없을 경우, 기존 문자열을 배열에 담아 반환  
  - value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환 
  - value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환
- `string.replace(from, to) `
  - 문자열에 from 값이 존재할 경우, 1개만 to 값으로 교체하여 반환
- `string.replaceAll(from, to)` 
  - 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체하여 반환

- `string.trim() `
  - 문자열 시작과 끝의 모든 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환 
- `string.trimStart() `
  - 문자열 시작의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
-  `string.trimEnd() `
  -  문자열 끝의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환



### 배열(Arrays)

- 키와 속성들을 담고 있는 참조 타입의 객체
- 순서를 보장
- 주로 대괄호를 이용하여 생성, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array, length 형태로 접근 가능



```javascript
const numbers = [1,2,3,4,5]

console.log(numbers[0]) //1
console.log(numbers[-1]) //undefined
console.log(numbers.length) // 5
```



- `array.reverse()` 
  -  원본 배열의 요소들의 순서를 반대로 정렬

- `array.push() `
  - 배열의 가장 뒤에 요소 추가 
- `array.pop() `
  - 배열의 마지막 요소 제거
- `array.unshift()` 
  -  배열의 가장 앞에 요소 추가 
- `array.shift() `
  - 배열의 첫번째 요소 제거
- `array.includes(value)` 
  -  배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환
- `array.indexOf(value) `
  -  배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환
  - 만약 해당 값이 없을 경우 -1 반환
- `array.join([separator]) `
  -  배열의 모든 요소를 연결하여 반환 
  - separator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용

#### Spread operator

- spread operator를 사용하면 배열 내부에서 배열 전개 가능
- 얕은 복사에 활용 가능

```javascript
const array = [1, 2, 3]
const newArray = [0, ...array, 4]

console.log(newArray) // [0, 1, 2, 3, 4]
```



### 배열 관련 메서드

> 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

`array.forEach(callback(element[, index[,array]]))` 

-  콜백 함수는 3가지 매개변수
  - element: 배열의 요소 
  -  index: 배열 요소의 인덱스 
  - array: 배열 자체 

- 반환 값(return)이 없는 메서드



`array.map(callback(elemenet[,index[,array]]))`

- 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
- 기존 배열 전체를 다른 형태로 바꿀 때 유용



`array.filter(callback(elemenet[,index[,array]]))`

- 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 
- 기존 배열의 요소들을 필터링할 때 유용



`array.reduce(callback(elemenet[,index[,array]]))`

=> 누적되는 값을 계산

- reduce 메서드의 주요 매개변수 •
  - acc 
    - 이전 callback 함수의 반환 값이 누적되는 변수 
  - initialValue(optional) 
    -  최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값

```javascript
arrat.reduce((acc, element, index, array) => {
    //do something
}, initialValue)

const numbers = [1,2,3]

const result = number.reduce((acc,num)=> {
    return acc+ num
}, 0)
console.log(result)  //6
```



`array.find(callback(elemenet[,index[,array]]))`

- 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환



`array.some(callback(elemenet[,index[,array]]))`

- 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환

- 모든 요소가 통과하지 못하면 거짓 반환 
-  (참고) 빈 배열은 항상 거짓 반환



`array.every(callback(elemenet[,index[,array]]))`

- 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
-  하나의 요소라도 통과하지 못하면 거짓 반환



## 객체(Objects)

객체 정의와 특징

- 객체는 속성(property)의 집합, 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
- value는 모든 타입(함수 포함) 가능
- 객체 요소 접근은 점 또는 대괄호로 가능



- 메서드는 객체의 속성이 참조하는 함수
- 객체.메서드명()으로 호출 가능
- 메서드 내부에서 this 키워드가 객체를 의미

=>메서드로 arrow function 사용 금지

```javascript
const me = {
    name: 'eunbin'
    getName: function() {
        return this.name
    }
}
//undefined

me.getName()
'eunbin'
```


