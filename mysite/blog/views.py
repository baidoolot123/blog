from django.shortcuts import render
from .models import Post
from .models import Author 
from .models import Books
#GET
#POST 
def login(request):
    if request.method == 'GET':
        return render(request, 'blog/login.html')
    else:
        pass 

# Create your views here.
# def index(request): 
#     posts = Post.objects.all()
#     return render(request, 'index.html', {"posts": posts})

def post_list(request): 
    posts = Post.objects.filter(author__id=1)  #ORM - select * from posts 
    return render(request, 'blog/post_list.html', {"posts": posts})



def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors.html', {"authors": authors})

def recommended_books(request):
    books = Books.objects.all()
    return render(request, 'blog/recommended_books.html', {'books': books})



