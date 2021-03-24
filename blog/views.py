from django.shortcuts import render
from .models import Post
from .models import Author 
from .models import Books
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages 

#GET
#POST 
def user_login(request):
    if request.method == 'GET':
        form = LoginForm()

    else:
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid(): 
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, 'Ваш акканут заблокирован')
            else:
                messages.error(request, 'Неправильный ввод данных')

        
    return render(request, 'blog/login.html', {'login_form': form})
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



