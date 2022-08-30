📝복습

html : 문서의 구조

css : 스타일



💡Tip!!

!+enter 하면 html 생성됨 => emet

```html
<!-- <h2#kimbap+ul>li.blue*5 + enter 누르면 한 번에 입력-->
<h2#kimbap+ul>li.blue*5

<h2 id="kimbap"><span class="green">김밥</span> 목록</h2>
<!-- span => 내가 만약 어떤 부분을 css 적용하고싶다면(스타일을 입히려면) 마크업을 해야한다 그 때 span 사용 -->
```





## CSS 기본 스타일

#### 크기 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 크기가 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em (html기본이 16px => em이 32*2px)
  - (바로 위, 부모 요소에 대한)상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem(32px)
  - 상속의 영향을 받지 않음
  - 최상의 요소(html)의 사이즈를 기준으로 배수 단위 가짐
- viewport (제멋대로 변해서 자주 사용 X)



#### 색상 단위

- 색상 키워드
- RGB 색상
  - '#' + 16진수 표기법
  - rgb()
- HSL 색상
  - 색상, 채도, 명도
- rgba : alpha(투명도)



#### 선택자 유형

- 기본 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자 => 선택자? 무조건 클래스 주자



### CSS 적용 우선순위

1. 중요도 : 사용시 주의

   ` !importatnt` => 우선순위가 아예 망가짐

2. 우선 순위(Specificity)

   - 인라인 > id> class, 속성, pseudo-class > 요소,  pseudo-element

3.  CSS 파일 로딩 순서

```
  * : 가장 쉽다. 모든 것에 된다. 

  요소 선택 : *보다는 덜한데..

  클래스 : 요소보다는 덜한데..

  id : 문서 당 하나!

  인라인 스타일 : 너가 굳이 그렇게 하겠다면,
  우선순위가 높은 것이길 바라... 
  재사용도 못하고 완전 쓰레긴데...
  굳이굳이 그러고싶다면 우선순위 높여줄게

  !important : 어? 이거 썼어. 그러면 ㅇㅋ 
  너의 소스코드의 핵폭탄을 투하한다면야..
 
  => !important : 외부라이브러리에서 많이 쓰는 패턴
  왜? 외부라이브러리 입장에서는 내가 적용되야 이걸 쓰는 의미가 있으니까!
```





#### CSS 상속

- Text 관련 요소(font, color, text-align) **(상속 O)** => 상속이 안 되면 개별적으로 다 스타일 넣어줘야 됨

- Box model 관련 요소(width, height, margin)/position 관련 요소(position, top/right/bottom)  **(상속 X)**



### CSS 박스 모델

> 모든 요소는 **네모(박스 모델)**이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. **(좌측 상단에 배치)**

*오른쪽에서 왼쪽 (inline direction)*

*위에서 아래 (block direction)*



📝박스는 네 부분으로 구성

- margin(외부 여백) => 색X 여백이니깐
- border(경계선, 테두리)
- content(내용)
- padding(내부 여백)



클래스와 내용을 넣어야 박스 생성 가능

``` html
<style>
	.box{
	  margin: 1rem;
	  padding: 1rem;
	  background-color: bisque;
	  border: 1px solid black;
    }</style>
```



#### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 box-sizing을 border-box로 지정





## CSS Display

> display에 따라 크기와 위치가 달라진다.

- display :` block` (= 막다, 줄을 막으니깐 줄 바꿈)
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭 차지 
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  - div(블록 레벨 요소)
  - **너비를 가질 수 없다면 자동으로 부여되는 margin**
- display : `inline`
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지
  - width, height, **margin-top, margin-bottom 을 지정할 수 없음**(컨텐츠 너비 만큼만 사용 , 한 줄에 있어야 하기 때문)
  - 상하 여백은 line-height로 지정
  - span(인라인 레벨 요소)
  - **inline의 기본너비는 컨텐츠 너비만큼**



### display

- display : `inline-block`
  - inline처럼 한 줄에 표시할 수 있고, width, height, margin 속성 모두 지정 가능
- display : `none`
  - 화면에 표시하지 않고, 공간조차 부여되지 않음
  - visibility : hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다



*노랑공간 : 마진 /파랑공간 : 컨텐츠*

