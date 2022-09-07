## Grid System

> 요소들의 디자인과 배치에 도움을 주는 시스템

- 기본요소
  - column : 실제 컨텐츠를 포함하는 부분
  - Gutter : 칼럼과 칼럼 사이의 공간(사이 간격) - padding, margin
  - Container : column들을 담고 있는 공간



`gird-4`  `grid-8` : 4칸 , 8칸 차지

한 줄에 카드를 총 4개 배치 => grid 3

*12 col grid, 16 col grid는 있는데 왜 15col grid는 없지??*

=> 약수가 많아야 배치가 더 다양하다



- Boorstrap grid system은 flexbox로 제작됨
- container, rows, column으로 컨텐츠를 배치하고 정렬



✔기억해야 할 2가지!!

1. 12개의 column
2. 6개의 grid breakpoints(화면 너비(비율X)에 따라 어떻게 배치하는지 구분하는 기준점)



```html
<div class ="container">
  <div class="row">
    <div class="col"></div>
    <div class="col"></div>
    <div class="col"></div>
  </div>
</div>
```



```html
<!-- 총 6개 배치 가장 작은 화면 1개, 모바일 :2개, 태블릿 3개 pc 4개 -->

<div class="row my-3">
  <div class="col-12 col-sm-6 col-md-4 col-lg-3">
    <div class="box">col</div>
  </div>
</div>
<div class="row my-3">
  <div class="col-12 col-sm-6 col-md-4 col-lg-3">
    <div class="box">col</div>
  </div>
</div>
<div class="row my-3">
  <div class="col-12 col-sm-6 col-md-4 col-lg-3">
    <div class="box">col</div>
  </div>
</div>
<div class="row my-3">
  <div class="col-12 col-sm-6 col-md-4 col-lg-3">
    <div class="box">col</div>
  </div>
</div>
<div class="row my-3">
  <div class="col-12 col-sm-6 col-md-4 col-lg-3">
    <div class="box">col</div>
  </div>
</div>
<div class="row my-3">
  <div class="col-12 col-sm-6 col-md-4 col-lg-3">
    <div class="box">col</div>
  </div>
</div>
```



📝사이즈

`xs` < `sm` < `md` < `lg` < `xl`  < `xxl`



### OFFSET

```html
<div class="row my-3">
  <!-- 중간에 4칸을 비우겠다 -->
  <div class="col-4 offset-4">
    <div class="box">col-4</div>
  </div>
</div>
```



### @media 

> 최상위 코드나, @안에 중첩으로 작성, 쿼리를 직접 작성해서 바꿔야 함