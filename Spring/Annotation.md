**[질문1] 어노테이션을 사용하는 이유 (효과) 는 무엇일까?**

> **어노테이션이란?**
> 사전적 의미로는 주석이며, 자바에서는 @ 기호와 함께 사용되며, 소스코드에 추가해서 사용할 수 있는 메타 데이터의 일종이다.코드에 직접적인 영향을 미치지는 않지만 컴파일이나 런타임에 관련된 정보를 제공한다.

어노테이션의 효과

- 컴파일러에게 코드 작성 문법 에러를 체크하도록 정보를 제공
- 소프트웨어 개발툴이 빌드나 배치시 코드를 자동으로 생성할 수 있도록 정보 제공
- 실행시(런타임시)특정 기능을 실행하도록 정보를 제공

---

**[질문2] 나만의 어노테이션은 어떻게 만들 수 있을까?**

커스텀 어노테이션을 만들 때 몇가지 규칙이 있다.

1. 어노테이션 타입은 `@interface`로 정의 해야한다. 모든 어노테이션은 자동적으로 `java.lang.Annotation` 인터페이스를 상속하기 때문에 다른 클래스나 인터페이스를 상속 받으면 안된다.
2. 파라미터 멤버들의 접근자는 `public`이거나 `default`여야만 한다.
3. 파라미터 멤버들은 byte,short,char,int,float,double,boolean,의 기본타입과 String, Enum, Class, 어노테이션만 사용할 수 있다.
4. 클래스 메소드와 필드에 관한 어노테이션 정보를 얻고 싶으면, 리플렉션만 이용해서 얻을 수 있다. 다른 방법으로는 어노테이션 객체를 얻을 수 없다.

### 어노테이션 생성하기

1. `@interface` 사용하여 어노테이션을 정의

```java
public @interface MyAnnotaion {
}
```

2. 메타 어노테이션 선언

```java
@Target(ElementType.METHOD)   // 적용대상은 method
@Retention(RetentionPolicy.RUNTIME)  // 유지정책은 runtime,  컴파일 이후에도 JVM이 참조
@Inherited
@Documented

public @interface MyAnnotaion { // String 타입으로 사용 가능
  public String value();
}
```

3. 적용할 어노테이션 추가
추가적으로 적용할 어노테이션이 있으면 추가해준다. 우리는 @Api와 @MyAnnotaion라는 어노테이션을 공통으로 묶을 것이므로 이를 추가해준다.

```java
@Api
@RestController
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
@Target(ElementType.TYPE)
public @interface MyAnnotaion {
    String name() default "MyAnnotaion";
    String value();
}
 
```





4. 변수 추가
어노테이션에 값을 부여하기를 원한다면 변수를 다음과 같이 선언해줄 수 있다.

```java
@Api
@RestController
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
@Target(ElementType.TYPE)
public @interface MyAnnotaion {
    String name() default "MyAnnotaion";
    String value();
}
```







5. 적용하기
위와 같은 과정으로 어노테이션을 생성하였으면 이제 다음과 같이 적용할 수 있다.

```java
@RestControllerWithSwagger(value = "RestMemberController", name = "RestMemberController")
@RequiredArgsConstructor
@Test1
@RequestMapping("/member")
public class MyAnnotaion {

    private final MemberService memberService;

    @ApiOperation("멤버 목록 반환")
    @GetMapping("/list")
    public ResponseEntity<String> upload() {
        return ResponseEntity.ok(memberService.getList());
    }

}
```

_사용자 정의 어노테이션을 선언할 때 메타 어노테이션을 함께 사용할 수 있다._
`@Target`
어노테이션을 정의할 때 적용 대상을 지정하는 데 사용

`@Documented`
어노테이션 정보를 javadoc으로 작성된 문서에 포함시킴

`@Inherited`
어노테이션이 하위 클래스에 상속되도록 함

`@Retention`
어노테이션이 유지되는 기간을 정하기 위해 사용

`@Repeatable`
어노테이션을 반복해서 적용할 수 있도록 함

> 출처
> https://ittrue.tistory.com/158
> https://khs0806.tistory.com/27
> https://mangkyu.tistory.com/130
