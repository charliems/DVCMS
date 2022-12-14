# /grades/
from django.urls import path

from . import views

app_name = 'grades'
urlpatterns = [
    path('', views.GradeListView.as_view(), name='list'),
    path('<int:pk>/edit', views.GradeUpdateView.as_view(), name='edit'),
    path('new/', views.GradeCreateView.as_view(), name='create'),
    path('submit/', views.GradeSubmitView.as_view(), name='submit'),
]
