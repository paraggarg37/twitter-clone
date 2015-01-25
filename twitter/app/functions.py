from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import authenticate ,login
from app.models import *
from django.db.models import Q

from django.contrib.humanize.templatetags.humanize import naturaltime

class loginform():

    def checkUsernameAvailablity(self,email):
         try:
            User.objects.get(username=email)
            return 0
         except User.DoesNotExist:
             return 1

    def create_user(self,fname,lname,email,password):
        if(self.checkUsernameAvailablity(email)):
            user = User.objects.create_user(username =email, email =email,password = password,first_name=fname,last_name=lname)
            user.save()
            return {"success":"user created"}

        return {"error":"*User already exist"}

    def login(self,request,email,password):
        user = authenticate(username=email, password=password)
        if user is not None:

            if user.is_active:
                login(request, user)
                return {"success":"*User is valid, active and authenticated"}
            else:
                return {"error":"*The password is valid, but the account has been disabled!"}
        else:
                return {"error":"*The username or password was incorrect."}


class localsHelper:
        tweets = 0
        following = 0
        followers = 0
        isfollowing = 0
        def __init__(self,id):
            self.user = User.objects.get(pk=id)
        def update(self):
            self.followHelper  = FollowHelper(self.user)
            self.following = self.followHelper.getFollowingCount()
            self.followers = self.followHelper.getFollowersCount()

            self.tweetsHelper = tweetsHelper(self.user.pk)
            self.tweets = self.tweetsHelper.tweetCount()

        def profile(self,user):
            self.isfollowing = self.followHelper.check(user)



class FollowHelper:
    def __init__(self,user):
        self.user = user
    def getFollowing(self):
        self.following = Follow.objects.all().filter(follower = self.user)
        t = tuple(k.following for k in self.following)+(self.user,)
        return t
    def getFollowers(self):
        self.followers = Follow.objects.all().filter(following = self.user)
        t = tuple(k.follower for k in self.followers)

        return t
    def getFollowingCount(self):
        return Follow.objects.all().filter(follower = self.user).count()
    def getFollowersCount(self):
        return Follow.objects.all().filter(following = self.user).count()

    def FollowingJSON(self):
        users = self.getFollowing()
        return  serializers.serialize("json",users,relations=('username','first_name','last_name','email',))
    def FollowersJSON(self):
         users = self.getFollowers()
         return  serializers.serialize("json",users,relations=('username','first_name','last_name','email',))

    def check(self,u):
        return Follow.objects.all().filter(following =self.user,follower = u).count()
    def followunfollow(self,user, op):
        if op == "follow":
            f = Follow(follower = self.user,following=user)
            f.save()
        else:
            f = Follow.objects.all().filter(following =user,follower =self.user)
            f.delete()

        return {"success":"done"}






class tweetsHelper:
    def __init__(self,id):
        self.user_id = id
        self.user = User.objects.get(pk=id)

    def timpestamp(self):

        for t in self.tweets:
            t.stamp = naturaltime(t.created)
            #t.timestamp = naturaltime(t.created)

        return self.tweets

    def get(self,user_type):


        if user_type=="following":
             self.users = FollowHelper(self.user).getFollowing();
        else:
             self.users = [self.user]

        self.tweets = Tweets.objects.all().filter(user__in = self.users).order_by('-created')

        k = self.timpestamp()
        return serializers.serialize("json",k,relations={'user':{'fields':('username','first_name','last_name','email',)}})

    def post(self,tweet):

        self.tweet  = Tweets(user = self.user,tweet=tweet)
        self.tweet.save()
        return {"success":"tweet posted"}

    def tweetCount(self):

        return Tweets.objects.all().filter(user = self.user).count()


class userHelper:
    def __init__(self,id):
        self.user = User.objects.get(pk=id)
    def getUser(self):
        return self.user
    def getUsersLike(self,string):

        firstname = string
        lastname = string

        name = string.split(" ")
        if(len(name) == 2):
            firstname = name[0]
            lastname = name[1]
            users = User.objects.all().filter( Q(first_name__icontains = firstname, last_name__icontains = lastname ) )[:5]
        else:
            users = User.objects.all().filter(Q(first_name__icontains = firstname) | Q(last_name__icontains = lastname) )[:5]


        return  serializers.serialize("json",users,relations=('username','first_name','last_name','email',))


