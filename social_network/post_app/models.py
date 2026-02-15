from django.db import models
from user_app.models import Profile


class Post(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/posts')
    author = models.ForeignKey(Profile, on_delete= models.CASCADE)

    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return f'{self.title}. Автор: {self.author.user}'

class Tag(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name