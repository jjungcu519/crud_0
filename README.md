## 개념개념
- 객체 관계 매핑 ORM
    - 파이썬 문법을 RDBMS가 알아듣도록 SQL로 변경해줌?
- 관계형 데이터베이스 관리 시스템 RDBMS
- 오라클 ORACLE

## Model
1. 모델 정의
*models.py*
```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```
2. 번역본 생성
```bash
python manage.py makemigrations
```
- 0001_initial.py -> 사용자로부터 받은 정보를 데이터베이스화 하기 위한 규칙을 세팅

3. DB에 반영 (2x2 형태의 표 생성)
```bash
python manage.py migrate
```

4. superuser 생성
```bash
python manage.py createsuperuser
```

5. admin에 모델 등록
```python
from django.contrib import admin
from .models import Post
admin.site.register(Post)
```