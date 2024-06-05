from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followUser")
    userfollowing = models.ManyToManyField(User, related_name="follower", blank=True)

    def __str__(self):
        return self.user.username
class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    postContent = models.ImageField(upload_to= "post")
    postCaption = models.CharField(max_length=100, blank=True)
    postUser = models.ForeignKey(User, on_delete= models.CASCADE)
    postLike = models.ManyToManyField(User, related_name= "liked_post", blank= True)


class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length= 500, null=False)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'comments by {self.comment_user}'
    
class directMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    msgContent = models.CharField(max_length=40000)
    msgdate = models.DateField(auto_now=True)

    def __str__(self):
        return (f'msg by {self.sender}')


    
