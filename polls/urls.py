from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #add
    url(r'^add/$', views.add, name = 'add'),
    #edit
    url(r'^(?P<question_id>[0-9]+)/edit/$', views.edit, name = 'edit'),
    #del
    url(r'^(?P<question_id>[0-9]+)/delete/$', views.delete, name = 'delete')
]
