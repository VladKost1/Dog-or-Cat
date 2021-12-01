from django.urls import path
from . import views
urlpatterns = [
  path('', views.index, name='index'),
  path('recognize/<str:photo_id>/', views.recognize, name='recognize')

]