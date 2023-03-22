from django.urls import path
from oneyo.views import base_views

from . import views

app_name = 'oneyo'

urlpatterns = [
    path('', base_views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
]