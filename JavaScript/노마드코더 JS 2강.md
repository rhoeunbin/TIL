# 노마드코더 JS 2강

## 1. 시작

JS 파일을 열려면 index.html을 사용해서 연다.

=> 브라우저는 HTML을 열고, HTML이 CSS와 자바스크립트를 가져옴



```javascript
alert("hi");
```

```css
body {
  background-color: bisque;
}
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <!-- CSS -->
    <link rel="stylesheet" href="style.css" />
    <title>Document</title>
  </head>
  <body>
         <!-- JS : 일반적으로 끝에 명시 -->
      <script src="app.js"></script>
    </form>
  </body>
</html>
```



## 2. 데이터 타입

### number

```javascript
// integar : full number(정수)
2+2
=> 4

// float
1.5
```



### text

string : 처음부터 끝까지 문자로 이루어져있다

```javascript
"Hello" + "my name is eunbin" // js에서 문자 타입 입력 방법

=> "Hellomy name is eunbin"
```



## 3. valuable : 변수

```javascript
const a = 5; // 바뀌지 않은 값
const b = 2;

console.log(a + b);
console.log(a % b);
console.log(a / b);

const myName = "eunbin";
```

*const veryLongVariableName = 0
js에서는 camelCase를 보통 사용
python은 snake_case*



## 4. const, let

*변수 만들 때 let, const, var차이*

let 재선언 금지, 재할당 가능
const 재선언 금지, 재할당 금지
var 재선언 가능, 재할당 가능



## 5. Booleans

> => true/ false

```javascript
const amIFat = false; => false라는 값이 존재함 null 이랑 다름
const pmIFat = true;
console.log(amIFat)
=> 따옴표 사용 X / 로그인 확인 시 사용
```

**null과 false는 값이 다름=> false는 값 O / null는 값 X**

> undefined = 변수는 선언했지만 값을 할당하지는 않음(정의 X)
> null = 변수에 null(값이 없다)이 할당된다 (정의 O)



### null

> 변수에 아무것도 없음(비어있음)

```javascript
const amIFat = null;
```



### undefined 

>  존재하지 않는 것

```javascript
let something; 
console.log(something);
=> 결과 undefined (값을 주지 않아서 undefined로 나옴)
```





## 6. arrays

> 데이터를 나열하기 위한 방법 중 하나.
> 항상 [ ] 안에 콤마(,)로 데이터들을 나열한다. 변수도 쓰일 수 있고, boolean, text, 숫자 등 데이터 정렬이 가능하다.
> ex) const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];



```javascript
const mon = "mon";
const tue = "tue";
const wed = "wed";
const thu = "thu";
const fri = "fri";
const sat = "sat";

const daysOfWeek = mon+tue+wed+thu+fri+sat;
console.log(daysOfWeek)
=> montuewedthufrisat

// 배열로 만들면 인덱스로 부르기 편함
const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"]; 

const nonsense = [1, 2, "hello", false, null, true, undefined, 'eunbin' ];
// 배열에 들어갈 수 있는 변수들
```



만약, 위의 변수에서 5번째 element 값을 알려주세요. 라고 한다면 어떻게 출력해야 할까?

```javascript
const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"];

console.log(daysOfWeek[5])
=> sat
```

**컴퓨터는 숫자를 0부터 세기 때문에, “mon”은 0번째**

*JS의 주석처리는 //*



```javascript
// 위의 상태에서 daysOfWeek이란 변수에 하나의 값을 더 넣고 싶다면
daysOfWeek.push(“sun”)

const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
```

**array는 하나의 변수 안에 데이터의 list를 가지는 것. **

*const인데 값 추가할 수 있는 이유 => daysOfWeek = ["hi"]; 가 아니라 daysOfWeek.push(“sun”) 데이터 추가여서*

**다른 프로그래밍 언어에도 있는 가장 기초적이고 필수적인 데이터 구조! 값을 리스트로 정리하는 것**



## 7. Object

> property를 가진 데이터를 저장해주며, { } 를 사용

```javascript
const playerName = "eunbin"
const playerPoint = "10"
const playerFat = "true"
// 대신

const player = {
name : eunbin,
points : 10,
fat : true,
};

console.log(player);
```



```javascript
// property를 불러오는 방법은 2가지가 있다.

1. console.log(player.name); => eunbin

2. console.log(player["name"]); => eunbin
```



** property를 바꾸는 것은 가능하지만 선언된 object를 바꾸는 것은 불가능*

```javascript
const player = {
name : eunbin,
points : 10,
fat : true,
};

console.log(player); => 일종의 object
player.points = player.points + 15;
console.log(player.points);
--> 25
```



*property를 추가 할 수도 있다.*

```javascript
player.koreanName = "은빈";

--> {name: "eunbin", points: "10", fat: true, koreaName: "은빈"}
```



## 8. Function

> 코드를 캡슐화해서 계속 반복하는 것

```javascript
console.log("Hello my name is eunbin");
console.log("Hello my name is eun");
console.log("Hello my name is bin");
```

=> 코드가 복잡해짐



```javascript
function sayHello() {
  console.log("Hello");
}

sayHello();
// Hello까지는 가능하지만 매번 함수를 호출해야하고 이름 변경을 못함
// 그래서 사용하는 것 argument(인수)
```



## 9. argument

> function을 실행하는 동안 어떤 정보를 function에게 보낼 수 있는 방법 => () 소괄호 안의 값



```
Why do we use ‘arguments’ on functions?
- To send a value to a function.

Functions always have to receive arguments.
- No
```



```javascript
alert();
console.log();
```

=> 아무것도 나오지 않음 안에 argument가 있어야 함

```javascript
function sayHello() {
console.log();
}

sayHello("nico")
sayHello("dal")
sayHello("lynn")
```

아래의 코드로 고침

```javascript
function sayHello(nameOfPerson) {
console.log(nameOfPerson);
}

sayHello("nico")
sayHello("dal")
sayHello("lynn") // nameOfPerson은 "nico" "dal" "lynn" 을 받았다고 생각
```



*인수는 여러 개 받을 수 있음*

```javascript
function sayHello(nameOfPerson, age) {
console.log("hello, my name is" + nameOfPerson + "and I am" + age + "old");
}

sayHello("nico", 10)
sayHello("dal", 20)
sayHello("lynn", 30)

=> hello, my name is nico and I am 10 old
```



```javascript
function plus() {
    console.log(2 + 2)
}

plus(); // 4
```



```javascript
//
function plus(a, b) {
    console.log(a, b)
}

plus(); // undefined, undefined

//
function plus(a, b) {
    console.log(a + b)
}

plus();	// NaN(Not a number)

// answer
function plus(a, b) {
    console.log(a, b)
}

plus(8, 60); // 68
```



**function의 값은 function 안에서만 존재한다.**



Object 안에서 매개변수가 argument를 받는 방식

```javascript
const player = {
    name: "nico",
    sayHello: function(otherPersonsName) {
    console.log("Hello " + otherPersonsName + " nice to meet you!");
},
};
player.sayHello("lynn");
```



### calculator

```javascript
const calculator = {
    add: function (a, b) {
    console.log(a + b);
    },
    minus: function (a, b) {
        console.log(a - b);
    },
    div: function (a, b) {
        console.log (a / b);
    },
    multi: function (a, b) {
        console.log (a * b);
    },
    power: function (a, b) {
        console.log (a ** b);
        },
    };

calcultor.add(5, 1);
calcultor.minus(3, 2);
calcultor.div(4, 7);
calcultor.multi(5, 2);
calcultor.power(2, 8);
```

*console.log => colsole에 log 남기는 것 => 콘솔에 그냥 결과를 남기는 것* 



# 10. Return

*계산기 안에서 값을 콘솔로 보내는것이 아니라 return을 통해 함수를 호출한 녀석에게 다시 주어 그걸 갖고 또다른 함수를 호출하는데 쓴다(연산결과 자체가 변수에게 주어진다)*



```javascript
const krAge = calculateKrAge(age);
function calculateKrAge(ageOfForeigner) {
    return ageOfForeigner + 2;
}

const krAge = calculateKrAge(age);
console.log(krAge);
```



```javascript
const calculator = {
    add: function (a, b) {
    return a + b;
    },
    minus: function (a, b) {
        return a - b;
    },
    div: function (a, b) {
        return a / b;
    },
    times: function (a, b) {
        return a * b;
    },
    power: function (a, b) {
        return a ** b;
        },
    };

calcultor.add(5, 1); // 아무 결과가 일어나지 않음

const plusResult = calcultor.add(5, 1);
console.log(plusResult); // 결과 나옴

const plusResult = calcultor.add(5, 1);
const minusResult = calcultor.add(plusResult, 1);
const timesResult = calcultor.add(5, minusResult);

```

**console.log와 return의 차이**

`console.log` 값을 결과로 정의하지 않고, 단순 결과값을 콘솔창에 표시

`return` 다음의 결과로 함수의 값을 정의하고 함수 종료



# 11. Conditionals

> 조건문



### prompt(); 사용X

> 함수는 사용자에게 창을 띄어 값을 받음.

prompt();를 사용하면 답을 할때까지 코드의 실행을 멈추고, 매우 오래된 방법임. 별로 안이쁨. css로 바꾸지도 못함.

```javascript
const age = prompt("how old are you?");
console.log(age); // 작동 X 창에 값을 넣어야 함

console.log(typeof age);
// string
```

### typeof 

> typeof 라는 키워드를 쓰면 type 볼 수 있음 => prompt();에서 숫자를 입력해도 string이라고 뜬다. 

*string이 디폴트이기 때문*



=> 한 type로 받아서 다른 type로 바꾸는 작업을 해야한다. "15"-->15

### parseInt();

>  string -> number로 변환해주는 함수 

```javascript
console.log(typeof "15", typeof parseInt("15")); 
// string number
```

**숫자로 변환이 되야 비교 가능**
*참고로 "숫자"가 아닌게 입력되면 변환이 안됨 =>  NaN(not a number)*



```javascript
const age = parseInt(prompt("how old are you?"));

// prompt 함수 먼저 실행 후 parseInt 실행

console.log(age); // num이 나옴
```



### isNaN();

> num인지 아닌지 boolean으로 알려줌 

```javascript
const age = parseInt(prompt("how old are you?"));

console.log(isNaN(age)); // num이 나옴

if(condition){
    // condition === true
} else {
    // condition ===false
}
```



```javascript
if(condition){
    // condition === true
} else {
    // condition ===false
}

const age = parseInt(prompt("how old are you?"));
// const age = NaN;

if(isNaN(age)){
    console.log("please write a num");
} else {
    console.log("thank u for writing your age");
}
```

**condition은 boolean으로 판별가능해야 한다, (true , false)**



```javascript
// 음주 가능 나이 측정 계산기
if(isNaN(age)){
    console.log("please write a num");
} else if (age < 18) {
    console.log("you are too young");
} else if (age <= 18 && age <= 50) {
    console.log("you are too young");
} else {
    console.log("you can drink");
}
```

**else if 가 여러 개일 때 하나라도 true라면 else 작동 X **



### 비교연산자

**&& : and**

**|| : or**

```
true || true === true
false || true === true
true || false === true
false || false === false

true && true === true
false && true === false
true && false === false
false && false === false
```



#### ===

```
JS에서만 사용하는 연산자이며
== 은 값만을 비교하고
=== 은 유형도 비교하여 === 를 주로 사용하는걸 추천
ex)
0 == false ---> true
0 === false ---> false
```


