from django.conf.urls import patterns, url

from app import views
from django.views.generic import TemplateView

from views import authenticate,createnewuser

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^home$', views.home, name='home'),
    url(r'^create/$',createnewuser.as_view(),name="create"),

    url(r'^tweet$',views.tweet.as_view(),name="tweet"),

    url(r'^tweets$',views.tweets,name="tweets"),

    url(r'^following$',views.following,name="following"),
    url(r'^followers$',views.followers,name="followers"),

     url(r'^logout$',views.logoutuser,name="logout"),

    url(r'^followunfollow/$',views.followunfollow,name="followers"),



    url(r'^PeopleSearch$',views.PeopleSearch,name="PeopleSearch"),

    url(r'^authenticate/$',authenticate.as_view(),name='authenticate'),

    url(r'^(?P<username>[\w@\.]+)/$', views.profile, name='profile'),

     # ex: /polls/5/
    #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)