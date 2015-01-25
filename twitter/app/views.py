from django.shortcuts import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User

from django.http import Http404
from django.http import *
from django.views.generic import View
from app import functions
from functions import *

from app.models import *
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

@ensure_csrf_cookie
def index(request):
   return render_to_response('app/login.html', locals(), context_instance=RequestContext(request))


@ensure_csrf_cookie
def register(request):
   return render_to_response('app/register.html', locals(), context_instance=RequestContext(request))


class authenticate(View):

    def get(self, request, *args, **kwargs):
         return JsonResponse({'type': request.GET['email']})

    def post(self,request):

         return JsonResponse(loginform().login(request,request.POST['email'],request.POST['password']))

class createnewuser(View):
    def post(self,request):
         return JsonResponse(loginform().create_user(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password']))


@login_required(login_url='/')
def home(request):
    email = request.user.email
    user = request.user
    home = "active"
    local = localsHelper(user.pk)
    local.update()
    return render_to_response('app/main.html', locals(), context_instance=RequestContext(request))

def tweets(request):
    return JsonResponse(tweetsHelper(request.GET['user']).get(request.GET['tweets']),safe=False)

def following(request):
     user = User.objects.get(pk=request.GET['user'])
     return JsonResponse(FollowHelper(user).FollowingJSON(),safe=False)

def followers(request):
     user = User.objects.get(pk=request.GET['user'])
     return JsonResponse(FollowHelper(user).FollowersJSON(),safe=False)


class tweet(View):


    def post(self,request):

         out = tweetsHelper(request.user.id).post(request.POST['tweet'])
         return JsonResponse(out)


def PeopleSearch(request):
    return JsonResponse(userHelper(request.user.pk).getUsersLike(request.GET['query']),safe=False)

@login_required(login_url='/')
def profile(request,username):

    logged_in_user = request.user

    try:
        user = User.objects.get(username = username)

        local = localsHelper(user.pk)
        local.update()
        local.profile(logged_in_user)

        return render_to_response('app/profile.html', locals(), context_instance=RequestContext(request))
    except:
        return HttpResponse("user not found");

@login_required(login_url='/')
def followunfollow(request):
    user = User.objects.get(pk = request.GET['user'])
    op = request.GET['operation']

    return  JsonResponse(FollowHelper(request.user).followunfollow(user,op))
@login_required(login_url='/')
def logoutuser(request):
        logout(request)
        return redirect('/')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


