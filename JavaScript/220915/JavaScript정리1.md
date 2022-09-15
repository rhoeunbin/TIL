## JavaScript

JavaScript의 필요성

> 브라우저 화면을 '동적' 으로 만들기 위함
>
> 브라우저를 조작할 수 있는 유일한 언어



*파편화와 표준화*

- 제 1차 브라우저 전쟁 이후 수많은 브라우저에서 자체 자바스크립트 언어를 사용
- 결국 서로 다른 자바스크립트가 만들어 지면서 크로스 브라우징 이슈가 발생하여 웹 표준의 필요성 제기
- 크로스브라우징(Cross Browsing)
  - W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론
  - 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문



*책을 살 때 ES6+(요즘 표준)를 사야 함 



Vanilla JavaScript (일종의 밈)

- 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장
- ES6 이후 ,다양한 도구의 등장으로 순수 자바스크립트 활용의 증대



브라우저에서 할 수 있는 일

- DOM 조작
  - 문서(HTML조작)
- BOM 조작
  - navigator
- JavaScipt Core(ECMAScript)
  - 일종의 프로그래밍 문법



*BOM>DOM => 브라우저(BOM)과 그 내부의 문서(DOM)을 조작하기 위해 ECMAScript(JS)를 학습*



## DOM(Document Object Model)

> HTML, XML 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스



- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 구조화되어 있으며 각 요소는 객체(object) 로 취급
- 주요 객체 
  - window
  - document

DOM -  해석

- 파싱(Parsing)
  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정



BOM(Browser Object Model)

> 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공

- window 객체는 모든 브라우저로부터 지원 받으며 브라우저의 창(window)를 지칭



## DOM 조작- 개념

- Document는 문서 한 장(HTML)에 해당ㅎ고 이를 조작
- DOM 조작 순서
  1. 선택(Select)
  2. 변경(Manipulation)

-> HTML 내 문서에서 조작



### DOM 객체의 상속 구조

- EventTarget
  - Event Listner를 가질 수 있는 객체가 구현하는 DOM 인터페이스
- Node
  - 여러 가지 DOM 타입들이 상속하는 인터페이스
- Element
  - Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
  -  부모인 Node와 그 부모인 EventTarget의 속성을 상속 
- Document
  -  •브라우저가 불러온 웹 페이지를 나타냄 
  - DOM 트리의 진입점(entry point) 역할을 수행 
-  HTMLElement
  - 모든 종류의 HTML 요소 
  -  부모 element의 속성 상속



```html
<script>
  console.log('hello,jsl') 
  alert('js 학습이 시작')
</script>

  window.print() ->출력창 뜸
```

->console 에 찍혀 있음(자바스크립트 코드 작성 가능) -> console 창에서 코드 작성

자바스크립트는 변수 선언 시 키워드를 항상 선언해야 함



### DOM 선택

#### 선택 관련 메서드

`document.queryselector` 은 반드시 한 가지만

`document.queryselectorAll` 은 모든 결과 선택



`getElementById(id)` : id는 하나 (Element)

`getElementsByClassname(names) `: classname은 여러 개 (Elements)

`getElementsByTagname(name)` :



#### 선택 메서드별 반환 타입

1. 단일 element
   - `getElementById(id)`
   - `queryselector()`
2. HTMLCollection
   - `getElementsByTagname()`
   - `getElementsByClassname()`
3. NodeList
   - `queryselectorAll()`



#### HTMLCollection & NodeList

> 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열)

- HTMLCollection
  - name, id, index 속성으로 각 항목에 접근 가능
- NodeList
  -  index로만 각 항목에 접근 가능 
  - 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능
- 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만,  querySelectorAll()에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않음



#### Collection

- Live Collection
  - 문서가 바뀔 때 실시간으로 업데이트 됨
  - DOM의 변경사항을 실시간으로 collection에 반영
  - ex) HTMLCollection, NodeList
- Static Collection (non-live)
  - DOM이 변경되어도 collection 내용에는 영향을 주지 않음 
  -  querySelectorAll()의 반환 NodeList만 static collection



#### 변경 관련 메서드 (Creation)

- `document.createElement()`
  - 작성한 태그 명의 HTML 요소를 생성하여 반환



#### 변경 관련 메서드 (append DOM)

- `Element.append()`
  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입 
  -  여러 개의 Node 객체, DOMString을 추가 할 수 있음 
  -  반환 값이 없음
- `Node.appendChild()`
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능) 
  - 한번에 오직 하나의 Node만 추가할 수 있음 
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동



#### ParentNode.append() vs Node.appendChild()

-  append()를 사용하면 DOMString 객체를 추가할 수도 있지만, .appendChild()는 Node 객체만 허용 
- append()는 반환 값이 없지만, appendChild()는 추가된 Node 객체를 반환 
- append()는 여러 Node 객체와 문자열을 추가할 수 있지만, .appendChild()는 하나의 Node 객체만 추가할 수 있음



####  변경 관련 속성 (property)

- `Node.innerText`
  -   Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text) (사람이 읽을 수 있는 요소만 남김)
  -  즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현 
- `Element.innerHTML `
  - 요소(element) 내에 포함된 HTML 마크업을 반환 
  - [참고] XSS 공격에 취약하므로 사용 시 주의



- XSS (Cross-site Scripting)
  - 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입 해 공격하는 방법 
  - 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함



#### DOM 삭제 - 삭제 관련 메서드

- `ChildNode.remove()`
  - Node가 속한 트리에서 해당 Node를 제거
- `Node.removeChild()`
  - DOM에서 자식 Node를 제거하고 제거된 Node를 반환 
  -  Node는 인자로 들어가는 자식 Node의 부모 Node



#### DOM 속성 – 속성 관련 메서드

- `Element.setAttribute(name, value)`
  - 지정된 요소의 값을 설정 
  -  속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
- `Element.getAttribute(attributeName)`
  - 해당 요소의 지정된 값(문자열)을 반환 
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름





`a.innerText` : a 태그 안에 텍스트 추가

`a.innerHTML` : 바꾸기 가능하지만 버그를 만들 수 있어서 쓰면 안 됨



`body.removeChild()` : 노드 아래를 지움

`title.remove()` : 노드 자체를 지움



## JavaScript 문법 정리

> 대소문자 구별, 유니코드 문자셋 이용

- 명령문이 한 줄을 다 차지하면 `;` 필요 없음
- 한 줄에 두 개 이상의 명령문이 필요하다면 반드시 `;` 사용



`//` : 한 줄 주석

`/* */` : 여러 줄 주석



선언

`var` : 변수를 선언, 추가로 동시에 값을 초기화

`let` : 블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화

`const` : 블록 스코프 읽기 전용 상수를 선언



변수 

> 값에 상징적인 이름으로 변수 사용



```javascript
var a;
console.log('a 값은 ' + a); // a 값은 undefined

console.log('b 값은 ' + b); // b 값은 undefined
var b;
// 이것은 아래의 '변수 호이스팅'을 읽기 전에는 혼란스러울 수 있음

console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined

let x;
console.log('x 값은 ' + x); // x 값은 undefined

console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
let y;
```



- `undefined`를 사용하여 변수 값이 있는지 확인 가능(input 변수는 값이 할당되지 않았고 if문은 true)

```javascript
var input;
if(input === undefined) {
  doThis();
} else {
  doThat();
}
```



- `undefined` 값은 불리언 맥락(context)에서 사용될 때 `false`로 동작

```javascript
var myArray = [];
if (!myArray[0]) myFunction();
```



- `undefined` 값은 수치 맥락에서 사용될 때 `NaN`으로 변환

```javascript
var a;
a + 2; // NaN으로 평가
```



- `null`값을 평가할 때, 수치 : `0`으로, 불리언 : `false`로 동작

```javascript
var n = null;
console.log(n * 32); // 콘솔에 0 으로 로그가 남음
```

