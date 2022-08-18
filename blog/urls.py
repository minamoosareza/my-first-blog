from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
	path('pastcourses_list/', views.pastcourses_list, name='pastcourses_list'),
	path('current_course/', views.current_course, name='current_course'),
	path('signup/', views.signup, name='signup'),
	path('past_course/', views.past_course, name='past_course'),
	path('articles_list/', views.articles_list, name='articles_list'),
	path('article/', views.article, name='article'),
	path('news_list/', views.news_list, name='news_list'),
	path('new/', views.new, name='new'),
	#path('post/<int:pk>/', views.post_detail, name='post_detail'),
	#path('post/new/', views.post_new, name='post_new'),
	#path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]