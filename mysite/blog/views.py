from django.shortcuts import render
from .models import Post
from .models import Author 
from .models import Books
from .models import Publish
from .forms import LoginForm, RegistrationForm, PublishForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.models import User 

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

def user_register(request):
    if request.method == 'GET':
        form = RegistrationForm()
    else: 
        form = RegistrationForm(request.POST)
        # cd = form.cleaned_data 
        user_exists = User.objects.filter(email=request.POST['email']).exists()
        if not user_exists: 
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.username = request.POST['email']
                new_user.save()
                Author.objects.create(user = new_user, first_name='', last_name='')
                return HttpResponseRedirect('/login/')
            else:
                messages.error(request, 'Неправильные данные!')
        else: 
            messages.error(request, 'Такой пользователь уже есть!')
    
    return render(request, 'blog/register.html', {'register_form': form})


def publish(request):
    if request.method == 'GET':
        form = PublishForm()
    else:
        form = PublishForm(request.POST)
    
    return render(request, 'blog/publish.html', {'publish_form': form})
    

def post_list(request): 
    posts = Post.objects.filter(author__id=1)  #ORM - select * from posts 
    return render(request, 'blog/post_list.html', {"posts": posts})



def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'blog/authors.html', {"authors": authors})

def recommended_books(request):
    books = Books.objects.all()
    return render(request, 'blog/recommended_books.html', {'books': books})

def publish(request):
    publish = Publish.objects.all()
    return render(request, 'blog/publish.html', {'publish': publish})



