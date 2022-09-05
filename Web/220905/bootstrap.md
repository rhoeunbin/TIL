## HTML 문서 구조화

- <thead>(header) <tbody>(body) <tfoot>(footer) 요소 활용 => 필수 요소는 아님

- 각각의 테이블을 <tr>로 묶고 <th>는 헤더 <td> 각각의 데이터 의미

=> colspan, rowspan = 병합한다



### table 태그 기본 구성

- thead
  - tr > th
- tbody
  - tr > td
- tfoot
  - tr > td
- caption : 표 설명 또는 제목



### Form 태그

> 아이디,비번/ 회원가입, 설문지
>
> 정보(데이터)를 서버에 제출하기 위해 사용되는 태그

기본 속성

- action : form을 처리할 서버의 URL(데이터를 보낼 곳)
- method : form을 제출할 때 사용할 HTTP 메서드 (GET or POST)
- enctype : method가 post인 경우 데이터의 유형



```html
<form action="/search" method="GET">
    
</form>
```



### input 

> : 다양한 타일을 가지는 입력 데이터 유형과 위젯 제공
>
> => 타입을 바꾸면 위젯이 바뀜

**display : inline** 



*속성*

- name : form control에 적용되는 이름 (이름/값 페어로 전송)
- value : form control에 적용되는 값 (이름/값 페어로 전송)
- required(필수 요소로 넣고 싶을 때), readonly, autofocus, autocomplete, disabled 등

```html
<form action="/search" method="GET">
    <input type="tet" name "q"> <-- 변수의 이름 지정 -->
</form>
    
<!-- 결과 http://www.google.com/search?q=HTML -->
```

**action은 서버로 제출되는 주소, q=HTML : 변수 이름 **



```html
<form action="/search" method="GET">
    username : <input type= "text" name"username"disabled>
    <!-- disable를 지우면 사용 가능할 때도 있음 -->
    name : <input type="text" name="name">
    password : <input type="password" name="name">
    <input type="submit" value="얍">
</form>
```

*input은 타입에 맞춰서 자동완성이 뜸*



### input label

>  label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음

- 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용 가능
- label과 id를 일치 시키면 상호 연관 시킴 (<input>에 id 속성, <label>에는 for 속성을 넣어서 상호 연관)



```html
<form action="/search" method="GET">
    <label for="username">username</label>
    <input type="email" name="username" id="username">
   <!--id는 반드시지정, label을 쓰면 정확한 곳을 터치하지 않아도 적용됨-->
    <label for="password">password</label>
    <input type="password" name="password" id="password">
</form>
```



#### input 유형

- text
- password
- email
- number
- file



#### 항목 중 선택

=> 동일한 항목에 대해 동일한 name을 지정하고 선택된 항목에 대한 value 지정

- checkbox : 다중 선택
-  radio : 단일 선택

*=> form은 서버에 데이터 전송하는 것으로 input으로 입력 받음, 사용자 입력값을 변수(name)으로 지정*



picker제공

- color : color picker
- date : name picker



hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값 설정

- hidden : 사용자에게 보이지 않는 input



# Bootstrap

> CDN (Content Delivery(Distribution) Network) 링크 활용

컨텐츠(CSS, JS) 등을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템 (가까운 서버를 통해 빠르게 전달, 외부서버를 활용함으로써 본인 서버의 부하가 적어짐)

=> 다운로드 없이 웹에서 제공해 주는 걸로 사용 가능(미리 작성된 CSS 가져와서 쓰는 느낌)



### spacing(Margin and padding)

```html
<!-- {property}{sides}-{size}-->

<div class="mt-3 ms-5">bootstrap-spacing</div>
<!-- class="mt-3"(margin-top) ms-5() mx(좌우) my(상하)-->
```



- `m` : margin
- `p` : padding



ex ) mt, mb, mx, my

ex ) ps, pt py



- `t` : top
- `b` : bottom
- `s` (start) : left(왼쪽에서 오른쪽)
- `e` (end) : right(오른쪽에서 왼쪽)
- `x` : 좌우
- `y` : 상하



- 0 - 0 rem - 0px
- 1 - 0.25 rem - 4px
- 2 - 0.5 rem - 8px
- 3 - 1 rem - 16px
- 4 - 1.5 rem - 24px
- 5 - 3 rem - 48px

=> 강제로 `!important` 쓰게 됨



```css
/* mx-0 : 왼쪽 오른쪽 마진이 0 */
.mx-0 {
margin-right: 0 !important;
margin-left: 0 !important;
}
```



```css
/* mx-auto : 블럭 요소 수평 중앙 정렬, 가로 가운데 정렬(인라인에서는 안 됨) */
.mx-auto {
margin-right: auto !important;
margin-left: auto !important;
}
```



```css
/* 위 아래 padding이 0 */
.py-0 {
padding-top: 0 !important;
padding-bottom: 0 !important;
}
```



### color

```css
:root {
  --primary: #007bff;
  --secondary: #6c757d;
  --success: #28a745;
  --info: #17a2b8;
  --warnung: #ffc107;
  --danger: #dc3545;
  --light: #f8f9fa;
  --dark: #343a40;
}
```



### Text

```html
<h2>Text</h2>
<p class="text-start">margin-top 3</p>
<p class="text-center">margin 4</p>
<p class="text-end">mx-auto, 가운데 정렬</p>
<a href="#" class="text-decoration-none">Non-underlined link</a>
<p class="fw-bold">Bold text.</p>
<p class="fw-normal">Normal weight text.</p>
<p class="fw-light">Light weight text.</p>
<p class="fst-italic">Italic text.</p>
```



📢추가사항

.은 class를 의미하는 것으로 쓸 필요 없음

opacity 투명도, 불투명도



sm 사이즈로 가면 화면 크기에 따라 변화

lg, md 태블릿 pc , sm 밑은 모바일 크기 정도(개발자 도구에서 확인 가능)



