from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    # path(r'data_set/', views.getData),
    path('', views.IndexApiView.as_view()),
]