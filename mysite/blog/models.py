from django.db import models
from django.utils import timezone 
from django.conf import settings 
from django.contrib.auth.models import User 


GENDER_OPTIONS = (
    ('M', 'Man'),
    ('W', 'Woman')
)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    birth_year = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, blank=True, null=True)   
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True) 

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title + ' Baidoolot'


class Books(models.Model):
    author = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    language = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 100)
    link = models.URLField()
    description = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'It is {self.name} written by {self.author}'


class Publish(models.Model):
    topic = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.topic}'
