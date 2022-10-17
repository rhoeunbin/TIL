## 이미지 파일 업로드 하기

`pip install Pillow`

`pip freeze >requirement.txt`

이미지 관리하기 위해서 => python image library라서 



```python
# models.py
class Article(models.Model):

	image = models.ImageField(upload_to='images/', blank=True)
```

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```



```python
#form.py에서 image field 추가

fields = [
    'title', 'content', 'image'
]
```



```python
# views.py에서 form넣을 위치에 

def create(reequest.POST, request.FILES)
# 이미지 올리기 가능
```



```python
# settings.py => 이미지를 서버에서 보여주는 방법

MEDIA_ROOT = BASE_DIRS/'images'
MEDIA_URL = 'media/'

```



```python
# urls.py에서

from django.conf import settings
from djano.congf.urls.static import static

urlpatterns = [
 ...   
] + static(Settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



*server가 하는 일=> file serving*



## image Resizing

> 이미지마다 파일 크기가 다르기 때문



`pip install django-imagekit`



```python
# settings.py
INASTALLED = [
    'imagekit',
]
```





```python
# models.py

class Article(models.Model):
    image = ProcessedImageField(upload_to='images/', blank=True,
                               processors=[ResizeTofill(400,300)],
                               format='JPEG',
                               options={'quality':80})
# 화질 저하가 되어서 올라옴
```



**file 안 나오면 views.py 에서   request.FILES 추가하기**