from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,)
    body = models.TextField(default="Default Text")
    
    def __str__(self):
        return self.title

