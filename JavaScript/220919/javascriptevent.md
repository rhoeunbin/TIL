## Event

> 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

- Event 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
  - 특정 메서드를 호출(`Element.click()`) 하여 프로그래밍적으로도 만들어 낼 수 있음

*load, mouseover, keydown, click*

- Event의 역할
  - ~하면~한다 
  - 클릭하면 경고창을 띄운다 
  - 특정 이벤트가 발생하면, 할 일(함수)을 등록
  - 대상에 특정 이벤트가 발생하면, 할 일을 등록





### in add eventlistner



`EventTarget.addEventListner()`

- 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
- 이벤트를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능



`target.addEventListener(type,listner[,options])`

- type
  - 반응 할 이벤트 유형(대소문자 구분 문자열)

- listner
  - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
  - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함



```html
<body>
    <button id="btn">버튼</button>
    <script>
        // ID가 btn인 요소 선택
        const btn = document.quertySelector('#btn')
        console.log(btn) // 파이썬에서의 print
        
        //btn이 클릭 되었을 때마다 함수가 실행
        btn.addEventListner('click',function(){
            console.log('버튼 클릭!')
        })
    </script>
</body>
```



- 클릭 시 1씩 증가시키는 코드

```html
<body>
    <button id="btn">버튼</button>
    <p id="counter">0</p>
    <script>
        //초기값
        let countNumber = 0
        
        // ID가 btn인 요소 선택
        const btn = document.quertySelector('#btn')
        console.log(btn) // 파이썬에서의 print
        
        //btn이 클릭 되었을 때마다 함수가 실행
        btn.addEventListner('click',function(){
            console.log('버튼 클릭!')
            //countNumber를 증가시키고
            countNumber += 1
            //id가 counter인 내용을 변경
            const counter = document.querySelector('#counter')
            counter.innerText = counterNumber
            
        })
    </script>
</body>
```



- 내용을 입력하면 값을 받아오고 싶다 => input

```html
<body>
    <input type="text" id="text-input">
    <script>
      // 1. input 선택
      const textInput = document.querySelector('#text-input')
      // 2. 
      textInput.addEventListner('input',function(event){
          // event => e로 바꾸기 가능
          //뭔가 입력된 내용을 받아오고 싶음 => input의 value 받아오기
          // input은 이벤트의 대상
          console.log(event)
          console.log(event.target.value)
          })
          // 3. 그대로 출력하기(아래 자동완성 7줄)
    </script>
</body>
```



## Event 취소

- event.preventDefault()
- 현재 이벤트의 기본 동작을 중단
- HTML 요소의 기본 동작을 작동하지 않게 막음
- 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소
- 취소 할 수 없는 이벤트도 존재
  - 이벤트의 취소 가능 여부는 event.concelable을 사용해 확인 가능



```html
<body>
  <h1>정말 중요한 내용</h1>
  <p>lorem dksdflk dkjsldfjskdf dksljkfdsld</p>
  <script>
      const h1 = document.querySelector('h1')
      h1.addEventListener('copy',function(event){
          // event의 기본 동작을 막고
          event.preventDefault()
          console.log('복사를 할 수 없음')
      })
      h1.addEventListener('drag',function(event){
          event.preventDefault()
          console.log('드래그 금지')
      })
  </script>
</body>
```



- Event 캡처링 : 하위 요소로 전파
- Event 버블링(일반적으로 막아야함): 상위 요소로 전파



```html
<h1>정말 <span>중요한</span> 내용</h1>
// span에 있는 거 전파 X
```



- 자바스크립트가 필요했던 modal

```html
<style>
    .modal-overlay {
        background-color:black;
        width: 100%;
        height: 100vh;
        /* position */
        position: fixed;
        top: 0;
        left: 0;
        /* 아직 전체화면 안 가짐 => top: 0; left: 0; 필요 */
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        /* 기본은 안 보이게 */
        display: none;
        opacity: 0;
    }
    .active {
        display: flex;        
    }
</style>

<body>
    <button id='modal-btn'>모달 버튼</button>
    <div class="nodal-overlay">모달</div>
    
    <script>
    const modalBtn = document.auerySelector('modal-btn')
    //모달 버튼이 클릭되면
    modalByn.addEventListner('click',function() {
        // 무엇이 바뀌면 좋을까?
        // class active 토글
        document.queryElector('#modal-content').class.toggle('active')
        })
        // 모달 취소 버튼이 클릭되면
        const modalCancleBtn = document.queryElector('#modal-cancel-btn')
        modalCancleBtn.addEventListener('click', function(){
            doeument.querySelector('#modal-content').classList.toggle('active')
            //X 버튼을 안 누르면 취소되지 않음 => 취소 버튼이 더 앞에 있기 때문에
        })
        
        //modalOverlay를 클릭하면 
        const modalOverlay = documnt.querySelector('#modal-content')
        modalOverlay.addEventListener('click',modalToggle) 
        })
    </script>
</body>
```



carousel 애니메이션 해보기

```html
<style>
    .carousel-items {
        display: flex;
        width :50rem;
    }
    .carousel-item {
        width :10rem;
        height: 10rem;
        background-color: bisque;
        dispaly: none;
    }
    .active {
        display :block;
        animation :active 1.5s;
    }
    /* 알아서 끌려오는 애니메이션 */
    @keyframes carousel-active{
        0% {
            transform: translateX(100%)
        }
        100% {
            transform: translateX(0)
        }
    }
</style>

<body>
    <div class="carousel-items">
        <div class="carousel-item active">1</div>
        <div class="carousel-item">2</div>
    </div>
    <button id="nextBtn">next</button>
    <script>
        const nextBtn = document.querySelector('#nextBtn')
        nextBtn.addEventListener('click',function(){
            //지금 active인 것을 어떻게 알지?
            const currentElement = document.querySelector('.active')
        })
        	//전체 item 중에.. 이 element의 인덱스?
        	const items = document.querySelectorAll('.carousel-item')
            const idx = [...items].indexOf(currentElement)
            console.log(currentElement, items, idx)
        	currentElement.classList.toggle('active')
        	
        
    </script>
</body>
```

