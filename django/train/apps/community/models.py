from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    posted_time=models.TimeField(default=timezone.now)
    #now the author got one to many relationship with the posts because the user can post many posts, and to do this in django we will put it as a foreign key
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)#we need to pass the on_deleted to tell django what to do if the user gets deleted, in this case we want the posts to be deleted.
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} on {self.post.content[:20]}: {self.content[:20]}'