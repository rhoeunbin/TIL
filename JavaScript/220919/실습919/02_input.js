
// 1. input 선택
const myTextInput = document.querySelector('#my-text-input')
// 2. input 이벤트 등록
myTextInput.addEventListener('input', function (event) {
  // input의 value를 받아오고 싶음
  // input은 이벤트의 대상!
  // // console.log(event)
  // console.log(e)
  // console.log(e.target.value)
  // 출력
  const myPtag = document.querySelector('#my-paragraph')
  myPtag.innerText = event.target.value
})
 