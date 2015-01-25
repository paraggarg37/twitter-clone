from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):

    uid = models.AutoField(primary_key=True,null=False)
    username = models.CharField(max_length=200,null = True)
    password = models.CharField(max_length=200,null = True)
    first_name = models.CharField(max_length=200,null = True)
    last_name = models.CharField(max_length=200,null = True)
    def __str__(self):

        return ' '.join([
            self.first_name
        ])


class Tweets(models.Model):
    tid = models.AutoField(primary_key=True,null=False)
    user = models.ForeignKey(User)
    tweet = models.CharField(max_length=140,null=True)
    created = models.DateTimeField(auto_now_add=True,null=False)
    stamp = models.CharField(max_length=50,null=True)


class Follow(models.Model):
    follower = models.ForeignKey(User,related_name="isfollowing")
    following = models.ForeignKey(User,related_name="tofollowed")
    class Meta:
        unique_together = (("follower", "following"),)