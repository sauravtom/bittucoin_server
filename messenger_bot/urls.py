from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^api/v1/$', views.MessengerBotView.as_view()),

]