from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/kitei/', views.tips_kitei, name='tips_kitei'),
	path('debug', views.debug_test, name='debug_test'),
	path('non', views.page_non, name='page_non'),
]
