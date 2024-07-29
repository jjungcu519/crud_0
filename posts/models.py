from django.db import models #모듈

# Create your models here.
class Post(models.Model): # Model 상속 설정?
    title = models.CharField(max_length=100) #title 에 글자가 들어올 수 있음을 정의해줌
