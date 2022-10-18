## RDB 테이블 간 관계

1:1

> 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련



1:N

> 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
>
> 기준 테이블에 따라(1:N)



M:N

> 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련
>
> 양쪽 모두에서 1:N



#### FK(foreign key)

- 키를 사용하여 부모 테이블의 유일한 값 참조(참조 무결성)
- 외래 키의 갑이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함



## 1:N(Article comment) => 댓글

> 댓글을 담당할 Article 모델은 1, comment 모델은 N

- 게시글은 댓글을 0개 이상 가짐
  - 게시글(1)은 여러 개의 댓글(N)을 가짐
  - 게시글 (1)은 댓글을 가지지 않을 수도 있음
- 댓글은 반드시 하나의 게시글에 속한다



### django relationship fields 종류

- OneToOneField()
- ForeignKey()
- MantToManyField()



### Foreign Key arguments - on_delete

- 외래 키가 참조하는 객체가 사라졌을 떄(게시글이 삭제 되면), 외래 키를 가진 객체를 어떻게 처리할 지 정의(댓글 어떻게?)
- 데이터 무결성을 위해서 매우 중요한 설정
- on_delete 옵션 값
  - CASCADE : 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
  - PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들이 존재
  - 수업에서는 CASCADE 값만 사용 예정



### comment 모델 정의 



1. *articles app에서*

- 댓글 목록 : 게시글 상세(articles:detail)
- 댓글 작성 : 게시글 상세(articles:detail)
- 생성 : DM 저장
- 생성 완료 후 => 게시글 상세

2. model
3. modelform



```python
# models.py

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    # 어차피 integer가 저장되는데 왜 굳이??
    # => 참조 대상은(직접 참조)comment.article 역참조는 article.comment_set
    # 만약 A라는 모델에 B모델의 FK를 정의하면 b.a_set
```





```python
# views.py 에서

def update(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
        'comments':article.comment_set.all()
    }
    return render(request, 'articles/index.html', context)
```



```html
<!-- detail.html -->

{% for comment in comments %}
<p>{{comment.content}}</p>
{% empty %}
<p>댓글이 없어용</p>
{% endfor %}
```



```python
# forms.py
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = [comment]
```



```python
# views.py 에서

def update(request,pk):
    article = Article.objects.get(pk=pk)
    
    comment_form = CommentForm()
    
    context = {
        'article':article,
        'comments':article.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'articles/index.html', context)
```



**article.comment_set.method()** 

- article 모델이 comment 모델을 참조(역참조)할 때 사용하는 매니저
- article.comment 형식으로는 댓글 객체 참조 X
- 대신 django가 역참조 할 수 있는 comment_cet manager를 자동으로 생성해 article.comment_Set 형태로 댓글 객체 참조 O
- 반면 참조 상황(Comment -> Article)에서는 실제 FK 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능



```html
<!-- detail.html -->

<form action="">
    {% bootstrap_form comment_form layout='inline' %}
    {% bootstrap_button button_type="submit" content="OK" %}
</form>
```



```python
# urls.py

path('<int:pk>/comments', views.comment_create, name="comment_create")
```



```python
# views.py

def comment_create(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # commit=False => 인스턴스만 생성됨, instance 직접 조작 가능
        # .save(commit=False) => 시점에서 modelform의 인스턴스
        comment.article = article
        comment.save() # 모델의 인스턴스
    # comment_form : CommentForm클래스의 인스턴스
    # comment : Comment 클래스의 인스턴스 
    # 모델폼의 save 메서드는 리턴 값이 그 모델의 인스턴스다
    return redirect('articles:detail',article.pk)
```



```html
<!-- detail.html -->

<form action="{% url 'articles:comment_form'%}" method="POST">
    {% csrf_token %}
    {% bootstrap_form comment_form layout='inline' %}
    {% bootstrap_button button_type="submit" content="OK" %}
</form>
```

