from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    first_name = models.CharField( max_length=15, blank = True)
    surname = models.CharField( max_length=30, blank = True)
    email_add = models.EmailField( max_length=254, blank = True, verbose_name = "email address")
    
    def save(self, *args, **kwargs):
        if not self.first_name and not self.surname: 
            self.first_name = "Anonymous"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.first_name} {self.surname} "


class Tag(models.Model):
    tags = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tags}"

class Post(models.Model):
    title = models.CharField(max_length=50, null = False)
    author = models.ForeignKey(Author, on_delete = models.SET_DEFAULT, default = "Anonymous", related_name = "posts")
    excerpt = models.CharField(max_length=200, null = False)
    image = models.ImageField(upload_to = "", null = True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique = True , default = "", null = False)
    content = models.TextField(null = False)
    tags = models.ManyToManyField(Tag)
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.title} {self.date}"
    
    
class Comment(models.Model):
    user_name = models.CharField(max_length=50, blank = True, )
    text = models.TextField(null = False, max_length = 300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "comments")
    
    def __str__(self):
        return f"{self.user_name} {self.post}"