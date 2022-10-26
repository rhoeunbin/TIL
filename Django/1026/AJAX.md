# AJAX

> 비동기식 JavaScript와 XML

*새로고침하지 않아도 알아서 다음 코드 실행*



 JS => *비동기식(Asynchronous)*

- 병렬적 Task 수행
- 요청을 보낸 후 응답을 기다리지 않고 다음 동작(코드 실행)이 이루어짐(non-blocking)

**요청이 오는 것 안 기다림(Web API 던저놓음) 그리고 그냥 다음 실행, 도착하면 무엇인가 함**

**자바스크립트의 비동기 처리란 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 자바스크립트의 특성**



```python
# python
import requests

response = requests.get('https://naver.com') # 요청이 도착할 때까지 기다렸다가 response에 저장하고 
print(response.text) # 그 다음 실행
```



### runtime

> Output =>  call stack => Web API => Task Queue (다시 stack으로)
>
> ex) 캐러쉘처럼 시간

```javascript
console.log('hi')

setTimeout(function(){
    console.log('작업중')
})
console.log('bye')

// hi출력 -> bye 출력-> 작업중 출력 순
```



### Event Loop 기반 동시성 모델

- Output
- Call Stack
- Web APi
- Task Queue



## Axios

- Promise based HTTP(도착하면 실행을 보내겠다)



```html
<body>
   <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
   <script>
    const URL = "https://jsonplaceholder.typicode.com/todos/1"
    axios.get(URL)
   	  .then(response => console.log(response.data))
      .catch(err => console.log('${err}!!!'))
    console.log('안녕')
    </script>
</body>
```



*화면을 그려볼 수 있음*

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <button>클릭</button>
    <!-- CDN, JS 항상 CDN 혹은 해당 파일 불러와야함 (npm을 활용해서 node 환경에서 개발하는 것은 지금과 전혀 다름 반드시 CDN으로 해야함-->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const body = document.querySelector('body')
    const title = document.createElement('h1')
    title.innerText = 'AJAX'
    body.appendChild(title)
      
<!-- 버튼 클릭 시마다 서버로 요청을 보내서 자동 새로고침 일어나게 -->
    const button = document.querySelector('button')
    // 버튼 클릭하면 함수 실행해줘
    button.addEventListener('click', function () {
      const URL = 'https://jsonplaceholder.typicode.com/todos/1'
      // axios는 URL로 요청 보내줌
      // 처리가 완료되면 ,실행시켜주겟다는 약속(promise)
      // 성공적이면 then, 실패면 catch
      axios.get(URL)
        .then(response => {
          // 성공해서 받은 응답 객체를  활용한 조작
          const h2 = document.createElement('h2')
          h2.innerText = response.data.title
          body.appendChild(h2)
          const p = document.createElement('p')
          p.innerText = response.data.userId
          body.appendChild(p)
        })
        .catch(err => console.log(`${err}!!!`))
    })
  </script>
</body>

</html>
```

 *기존 html : 사용자가 요청 -> html 응답  => Axios :비동기 요청 -> JSON 응답*



```html
<script>
    // 1. 좋아요 버튼
    const likeBtn = document.querySelector('#like-btn')
    // 2. 좋아요 버튼을 클릭하면 함수 실행
    likeBtn.addEventListner('click', function (){
    // 서버로 비동기 요청을 하고 싶음    
        axios({
            method: 'get',
            url: '/articles/${event.target.dataset.articlId}/like/'
        })
        .then(response => {
            console.log(response)
            console.log(response.data)
           // event.target.classList.toggle('bi-heart')
           // event.target.classList.toggle('bi-heart-fill')
            if (response.data.isliked === True){
                event.target.classList.add('bi-heart')
                event.target.classList.remove('bi-heart-fill')
            }else {
                event.target.classList.add('bi-heart')
                event.target.classList.remove('bi-heart-fill')
            }
            const likeCount = docoment.querySelector('#Like-count')
            likeCount.innerText = response.data.likeCount
        })
    })
    
</script>
```





```python
# views.py
from django.http import JsonResponse
@login_required
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,

        if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
            is_liked = True
       # return redirect('articles:detail', pk)
    	context = {'isLiked':is_liked, 'likeCount':article.like_users.count()}
    	return JsonResponse({'is_liked':'is_liked'})
```



### Promise

- 비동기 작업을 관리하는 객체
  - 미래의 완료 또는 실패와 그 결과 값을 나타냄
  - 미래의 어떤 상황에 대한 약속
- 성공(이행)에 대한 약속 `.then()`
- 실패(거절)에 대한 약속 `.catch()`



`.then(callback)`

- 이전 작업(promise)이 성공했을 때(이행했을 때) 수행할 작업을 나타내는 callback 함수 
- 그리고 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음 
- 따라서 성공했을 때의 코드를 callback 함수 안에 작성





`.catch(callback)`

- .then이 하나라도 실패하면(거부 되면) 동작 (동기식의 ‘try - except’ 구문과 유사) 
- 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있음



- 각각의 .then() 블록은 서로 다른 promise를 반환
  - 즉, .then()을 여러 개 사용(chaining)하여 연쇄적인 작업을 수행할 수 있음 
  - 결국 여러 비동기 작업을 차례대로 수행할 수 있다는 뜻
- • .then()과 .catch() 메서드는 모두 promise를 반환하기 때문에 chaining 가능

**반환 값이 반드시 있어야 함// 없다면 callback 함수가 이전의 promise 결과를 받을 수 없음**



`.finally(callback)`

-  Promise 객체를 반환 
- 결과와 상관없이 무조건 지정된 callback 함수가 실행
- 어떠한 인자도 전달받지 않음 
  - Promise가 성공되었는지 거절되었는지 판단할 수 없기 때문 
- 무조건 실행되어야 하는 절에서 활용
  -  .then()과 .catch() 블록에서의 코드 중복을 방지

- .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining) 
- callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음



## 비동기 적용하기

### follow

