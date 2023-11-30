

# 📌 Types of TS

✅ 배열: 자료형[]
✅ 숫자: number
✅ 문자열: string
✅ 논리: boolean
✅ optional



```typescript
const player : {
  name: string,
  age?:number
} = {
  name: "nico"
}

❌ player.age가 undefined일 가능성 알림
if(player.age < 10) {
}

⭕ player.age가 undefined일 가능성 체크
if(player.age && player.age < 10) {
}

❗ ?를 :앞에 붙이면 optional
```



### ✅ Alias(별칭) 타입

```typescript
type Player = {
  name: string,
  age?:number
}

const player : Player = {
  name: "nico"
}
```

⭐ 함수에서는 어떻게 쓸까

```typescript
type Player = {
  name: string,
  age?:number
}

function playerMaker1(name:string) : Player {
  return {
    name
  }
}

const playerMaker2 = (name:string) : Player => ({name})

const nico = playerMaker1("nico")
nico.age = 12
```



📌 Types of TS(part II)
### ✅ readonly 사용하기

```typescript
type Player = {
  readonly name:string
  age?:number
}

const playerMaker = (name: string): Player => ({name})

const nico = playerMaker("nico")
🚫 nico.name = "aa"

const numbers: readonly number[] = [1, 2, 3, 4]
```

*🚫 numbers.push(1)
❗ readonly가 있으면 최초 선언 후 수정 불가
  ⇒ immutability(불변성) 부여
    but, javascript에서는 그냥 배열*



### ✅ Tuple

> 정해진 개수와 순서에 따라 배열 선언

```typescript
const player: [string, number, boolean] = ["nico", 1, true]
// 요소의 개수 똑같이

❗ readonly도 사용가능 ⇒ readonly [...] 형태
const player: readonly [string, number, boolean] = ["nico", 1, true] 
```



### ✅ undefined, null, any
`any` : 아무 타입(비어있는 값들을 쓰면 기본값이 any가 됨) => ts를 빠져나오는 방법으로 추천X 
`undefined` : 선언X 할당X
`null` : 선언O 할당X





📌 Types of TS(part II)
### ✅ unknown

> 어떤 타입인지 모르는 변수

```typescript
let a:unknown;

let b = a + 1 // 오류 => a가 unknown이기 때문에

if(typeof a === 'number'){
  let b = a + 1
}
if(typeof a === 'string'){
  let b = a.toUpperCase()
}
```



### ✅ void

> 아무것도 return하지 않는 함수에서 반환 자료형(비어 있는 것)

```typescript
function hello():void { // 굳이 이렇게 쓸 필요 X

function hello() {
  console.log('x')
}
const a = hello()
🚫 a.toUpperCase() // toUpperCase는 void타입에 없음
```



### ✅ never

> 함수가 return하지 않을 때 => 많이 사용하진 않음

```typescript
function hello():never {
  throw new Error("zzz") // return하고 오류 발생시키는 
  🚫return "a"
}

function temp(name:string|number):never {
  if(typeof name === "string"){
    name
  } else if(typeof name === "number"){
    name
  } else {
    name
  }
}

```

*if 안에서는 string형의 name 반환
else if 안에서는 number형의 name 반환
else 안에서는 never형의 name 반환
⇒ 즉, 제대로 인자가 전달되었다면 else로 올 수 없음*





# 📌 Function

### ✅call signature

> 함수를 어떻게 호출해야할지, 함수의 반환 타입 알려줌



 {}를 사용했을 때 오류가 발생하는 이유

> **{}를 사용하면 그 값이 반환값이 함수 내부의 내용으로 처리**

```typescript
예시)
\1. const add:Add = (a,b) => a+b 를 함수로 풀면 다음과 같게 됩니다.
function add(a, b) {
return (a+b)
}

\2. const add:Add = (a,b) => {a+b} 를 함수로 풀면 다음과 같게 됩니다.
function add(a, b) {
a+b;
}
```



즉 애로우함수에서 {}를 사용하게 되면 그 안의 값은 반환이 아니라 함수 내부 내용으로 처리되기에 반환값이 없는 void로 처리됩니다. 이에 따라 위에서 미리 선안한 Add자료형의 반환값은 number라고정해놓은 내용과 충돌하기에 에러가 발생합니다.



\1. 화살표 함수에서 {}를 생략하면 return이 생략된 것
\2. 즉 a + b 와 { return a+b } 는 같은 뜻
\3. {a+b}라고 하면 아무것도 리턴하지 않기 때문에 에러남



type이 any 뜨면

npm install -g typescript 입력후
tsc --init 입력해보시고 다시 시도해보기



### ✅Overloading

> Function(=Method) Overloading은 직접 작성하기보다 외부 라이브러리에 자주 보이는 형태로, 하나의 함수가 복수의 Call Signature를 가질 때 발생한다



```typescript
// 데이터 타입이 다른 경우

type Add = {
    (a: number, b: number): number,
    (a: number, b: string): number // b의 타입이 다름!
}

const add: Add = (a, b) => {
    if (typeof b === "string") return a;
    return a + b;
}
```



```typescript
// 예를 들어, Next.js의 라우터 push가 대충 두 가지 방법으로 페이지를 이동한다고 할 때,

router.push("/home");

router.push({
path: "/home",
state: 1
});
```



```typescript
// 패키지나 라이브러리는 위와 같이 두 가지 경우의 Overloading으로 디자인되어 있을 것이다

type Config = {
    path: string,
    state: number
}

// Config의 타입 지정 각각 해야함
type Push = {
    (path: string): void
    (config: Config): void
}

const push: Push = (config) => {
    if (typeof config === "string") {console.log(config)};
    else {
        console.log(config.path, config.state);
    }
}
```





```typescript
// 파라미터의 개수가 다를 때

type Add = {
    (a:number, b:number): number
    (a:number, b:number, c:number): number,
}

🚫const add:Add = (a, b, c) => { // 마지막에 적힌 c가 옵션이라는 것을 의미

const add:Add = (a, b, c?:number) => {
    if(c) return a + b + c
    return a + b
}
```



### ✅ Polymorphism(다형성)

> poly란?  - many, serveral, much, multi 등과 같은 뜻
> morphos란? - form, structure 등과 같은 뜻
> polymorphos = poly + morphos = 여러 다른 구조

```typescript
// 배열의 요소 하나씩 print
type SuperPrint = {
    (arr: number[]):void // 받고 싶은 객체의 타입을 지정해야 함
    (arr: boolean[]):void
    (arr: string[]):void
}

const superPrint: SuperPrint = (arr) => {
  arr.forEach(i => console.log(i))
}

superPrint([1, 2, 3, 4])
superPrint([true, false, true])
superPrint(["a", "b", "C")
```

**concrete type**
\- number, boolean, void 등 지금까지 배운 타입



**generic type**

> 들어올 타입을 정확히 모를 때 사용
>
> 타입의 placeholder

```typescript
type SuperPrint = { 
    <TypePlaceholder>(arr: TypePlaceholder[]): void 
}
// const superPrint: <string | number | boolean>(arr: (string | number| boolean) void) 가 된다

const superPrint: SuperPrint = (arr) => {
  arr.forEach(i => console.log(i))
}

superPrint([1, 2, false, true, "hello"]) // 다 가능
```





```typescript
// superPrint의 리턴 타입을 바꾸고 싶다면

type SuperPrint = { 
    <TypePlaceholder>(arr: TypePlaceholder[]): TypePlaceholder
}
// const superPrint: <string | number | boolean>(arr: (string | number| boolean) void) 가 된다

const superPrint: SuperPrint = (arr) => arr[0]

const a = superPrint([1, 2, 3, 4]) // number
const b = superPrint([true, false, true]) // boolean
const c = superPrint(["a", "b", "C") // string
const d = superPrint([1, 2, false, true, "hello"]) // string | number| boolean
```



```typescript
type Words = { // 해시
    [key: string]: (string | string[])
    //객체의 property에 대해 모르지만 타입만을 알 때 유용
}
class Dict {
    private words: Words // constructor에 포함시켜줘야 함
    constructor() {
        this.words = {}
    }
    add(word: Word) { // word는 Word 클래스의 인스턴스 타입.
        if(!this.words[word.term]) {
        // 사전에 없는 단어이면
            this.words[word.term] = word.def;
        }
	}
    def(term:string){
        return this.words[term];
    }
    // 직접 해보기
    // 단어를 삭제
    rmv(term: string) {
    	delete this.words[term];
    }
    // 단어 이름 업데이트
    update(oldTerm: string, newTerm: string) {
        if(this.words.hasOwnProperty(oldTerm)) {
            this.words[newTerm] = this.words[oldTerm];
            delete this.words[oldTerm];
        }
    }
    // 사전에 저장된 단어의 개수
    size() {
    	return Object.keys(this.words).length;
    }
    // 모든 사전의 이름과 뜻 출력
    all() {
        for(let [key, value] of Object.entries(this.words)) {
        console.log(`${key}: ${value}`)
        }
    }
}
// words는 initializer 없이 선언해주고 contructor에서 수동으로 초기화
// constructor에 인자로 넣어 constructor가 지정해주길 바라는 게 아니므로
}

// 각각의 단어에 대한 클래스
class Word {
    private words: Words // constructor에 포함시켜줘야 함
    constructor(
    	public term:string,
        public def :string
        ) {}
    // 단어 출력하는 메소드
    toString() {
    	console.log(`${this.term}: [뜻] ${this.def}`);
    }
    // 단어 정의 추가
    addDef(newDef : string) {
        if(typeof this.def === 'string') {
            this.def = [this.def, newDef]
        } else {
            this.def = [...this.def, newDef];
        }
    }
    // 단어 정의 수정
    updateDef(oldDef : string, newDef: string) {
        if(typeof this.def === 'string') {
            if(oldDef === this.def) this.def = newDef
            } else {
                this.def.filter(val => val !== oldDef);
                this.def.push(newDef);
            }
        }
    }
}


/** 출력 */
const kimchi = new Word("kimchi", "한국의 음식");
const tang = new Word("연근 갈비탕", "중국의 음식");
const sushi = new Word("스시", "일본의 음식");
kimchi.addDef("고춧가루로 배추를 버무려 숙성 및 발효시킨 음식")
kimchi.toString(); // kimchi: 한국의 음식,고춧가루로 배추를 버무려 숙성 및 발효시킨 음식
tang.toString() // 연근 갈비탕: 중국의 음식
sushi.updateDef("일본의 음식", "밥을 뭉쳐놓고 그 위에 재료를 얹어낸 음식");
sushi.toString(); // 스시: 밥을 뭉쳐놓고 그 위에 재료를 얹어낸 음식

const dict = new Dict();
dict.add(kimchi);
dict.def("kimchi") // 한국의 음식

dict.add(tang);
dict.add(sushi);
dict.all()
// kimchi: 한국의 음식,고춧가루로 배추를 버무려 숙성 및 발효시킨 음식
// 연근 갈비탕: 중국의 음식
// 스시: 밥을 뭉쳐놓고 그 위에 재료를 얹어낸 음식
dict.find("kimchi");
// (2) ['한국의 음식', '고춧가루로 배추를 버무려 숙성 및 발효시킨 음식']
dict.size()
// 3
dict.update("kimchi", "김치")
dict.all()
// 연근 갈비탕: 중국의 음식
// 스시: 밥을 뭉쳐놓고 그 위에 재료를 얹어낸 음식
// 김치: 한국의 음식,고춧가루로 배추를 버무려 숙성 및 발효시킨 음식
dict.rmv("연근 갈비탕");
dict.all()
// 스시: 밥을 뭉쳐놓고 그 위에 재료를 얹어낸 음식
// 김치: 한국의 음식,고춧가루로 배추를 버무려 숙성 및 발효시킨 음식
```



### Interface

```typescript
// public이지만 모두 수정할 수 없게 하려면 readonly
class Word {
    private words: Words // constructor에 포함시켜줘야 함
    constructor(
    	readonly public term:string,
        readonly public def :string
        ) {}
```



```typescript
// 타입 설명 방식
// 1. 별칭 사용
type Nickname = string
type Health = number
type Friends = Array[string]

type Player = {
    nickname:Nickname,
    healthBar:number
}


// 2. 그냥 타입 지정
type Player = {
    nickname:string,
    healthBar:number
}

const nico : Player = {
    nickname:"nico",
    healthBar:10
}

// 3. 바로 타입 써주기
type Food = string;

const kimchi:Food = "delicious"


// 타입을 특정 값만 가지게 하는 방법

type Team = "red" | "blue"| "yellow" // 타입을 특정 값만 가지게 할 수 있음
type Player = {
    nickname:string,
    team:Team // red, blue, yellow 중 하나만 가능
}

const nico:Player{
    nickname:"nico"
    team;"pink"
}
```



오브젝트 모양을 써주는 방법 두가지 => interface

```typescript
// 1 interface => 오로지 로브젝트의 모양을 ts에게 설명해주기 위해서만 사용됨
type Team = "red" | "blue"| "yellow"
type Health = 1 | 5 | 10
interface Player {
    nickname:string,
    team:Team,
    health: Heahth
}

// interface Hello = string 이런거는 불가능

// 2 type => interface에 비해 활용이 높음
type Player = {
    nickname:string,
    team:Team 
    health: Heahth
}
```



Type의 용도 :
\1. 특정 값이나 객체의 값에 대한 타입을 지정해줄 수 있다.
\2. Type alias(타입에 대한 별명)를 만들어줄 수 있다.
\3. 타입을 특정한 값을 가지도록 제한할 수 있다.

타입과 인터페이스의 차이점은 type 키워드는 interface 키워드에 비해서 좀 더 활용할 수 있는 것이 많다는 것이다.(type 키워드는 다양한 목적으로 사용될 수 있음)

즉, interface는 오로지 객체의 형태를 타입스크립트에게 설명해주기 위한 용도로만 사용

interface는 위와 같이 상속의 개념을 사용할 수 있다 (오른쪽은 type을 이용하여 상속한 방법)
⇒ 문법 구조가 객체지향 프로그래밍의 개념을 활용 ⭐️

인터페이스의 또 다른 특징으로는 속성(Property)들을 ‘축적’시킬 수 있다는 것이다.

 

```typescript
interface User {
    name:string
}

interface Player extends User{
    
}

const nico : Player = {
    name :"nico"
}
```





```typescript
//추상 클래스는 이것을 상속받는 다른 클래스가 가질 property와 메소드를 지정하도록 함
abstract class User {
    constructor(
    	protected firstName:String,
        protected lastName:String,
    )
    abstract sayHi(name:string):string
    abstract fullName():string
}
// 추상 클래스는 그것으로 인스턴스를 만드는 것을 허용하지 않음
new User() // 불가능


class Player extends User {
    // sayHi, fullName 구현하라고 나옴
    fullName(){
        return '${this.firstName} ${this.lastName}'
    }
    sayHi(name:string){
        return 'Hello ${name} my name is ${this.fullName()}'
    }
    
}
```



*abstract로 상속받은 클래스를 js로 변환하게되면, abstract코드도 js파일에 남게된다.*

*그래서 코드 최적화를 위해, interface와 implements를 사용한다. 이 두 기능은 js에는 없으므로 ts를 js로 변환한 코드에서 보이지 않는다. 즉 코드최적화 완료 => abstract와 interface/implements는 둘다 같은 기능을 구현한다.(상속받는 클래스가 구현할 기능들을 명시함)*



```typescript
interface User {
    firstName:string,
    lastName:string,
    sayHi(name:string):string
    fullName():string
}

interface Human{
    health:number
}

class Player implements User, Human { // 인터페이스를 상속할 때에는 property를 private, protected로 만들지 못함 => public으로 해야함
    constructor(
        public firstName:string,
    	public firstName:string,
    ){
    fullName(){
        return '${this.firstName} ${this.lastName}'
    }
    sayHi(name:string){
        return 'Hello ${name} my name is ${this.fullName()}'
    }
}
    
function makeUser(user: User){
    return "hi"      
}
makeUser({
    firstName:"nico",
    lastName:"las",
    sayHi: (name) =>"string"
    fullName: ()=>"xx"
})
```



### Polymorphism(다형성)

> 다른 모양의 코드를 가질 수 있게 하는 것 => generic사용(placeholder 타입 쓸 수 있게 함)

```typescript
// Storage는 이미 정의되어 있어 여기서 Storage를 선언하면 오버라이딩이 일어나게 될 것이다.
// 따라서 나만의 인터페이스를 갖고 싶다면 SStorage 사용
interface SStorage<T>{ // storage 이미 정의되어있음
    [key:string]:T // key가 제한되지 않은 string 정의해줌
}
 
class LocalStorage<T>{
	private storage: SStorage={}
	set(key:string, value:T){ // set메서드
        if(this.storage[key]!=undefined)
    console.log("Error: already exist!");
    else 
    this.storage[key]=value;
        }
    remove(key:string){
    delete this.storage[key];
    }
    get(key:string):T{
    	if(this.storage[key]==undefined)
    {
    console.log("Error: Dosen't exist!");
    // return default;
    //자동으로 undefined가 반환되며 에러도 없음.
    //받는 쪽에서 undefined인지 검사할 필요가 있음.
    }
    return this.storage[key];
    }
    clear(){
    	this.storage={}
    }
}

const stringStorage = new LocalStorage<string>();
// stringStorage는 string 타입의 로컬 스트리지임

console.log(stringStorage.get(""));
stringStorage.get() // generic을 바탕으로 call signature 만들어줌 => get(key: string): string => ts가 concrete 타입으로 만들어 주기 때문
stringStorage.set("hello", "How are you?");

const booleanStorage = new LocalStorage<boolean>();
booleanStorage.get("xxx");
booleanStorage.set("ready?", true); // value는 boolean으로 되어야 함
```

