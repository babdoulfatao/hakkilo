from django.urls import path
from . import views
import include
from rest_framework.urls import urlpatterns


urlpatterns = [
    path('', views.mainpage.as_view()),
    path('api/chatbot/', views.chatbotViews.as_view()),
    path('intent', views.intentAPIView.as_view())

]