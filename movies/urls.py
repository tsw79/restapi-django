# from django.conf.urls import url 
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies import views 
 
urlpatterns = [ 
  path('movies/', views.MovieList.as_view()),
  path('movies/<pk>/', views.MovieDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)