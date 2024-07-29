from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, 'index.html', context) #모든 게시물을 보여주는 페이지로 활용

def detail(request, id): #파랑은 변수, 노랑은 실제 컬럼값을 의미?
    post = Post.objects.get(id=id)

    context = {
        'post' : post,
    }

    return render(request, 'detail.html', context)