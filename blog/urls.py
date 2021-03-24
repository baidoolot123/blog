from django.urls import include, path 
from . import views 

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # path('index/', views.index, name = 'main-view')
    path('', views.post_list,name = 'post_list'),
    path('authors/', views.authors_list, name='authors_list'),
    path('books/', views.recommended_books, name='books'),
    path('login/', views.user_login, name = 'login')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

