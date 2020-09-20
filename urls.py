from django.urls import path, include, re_path

from . import views

urlpatterns = [
    

	#path('register/', views.register, name='register'),
	path("", views.index_login, name="index_login"),
	path('index/', views.index, name='index'),
	path("phone-filter/", views.phone_filter, name='phone-filter'),
	path("index2/", views.index2, name="index2"),
	path('index3/', views.index3, name='index3'),
	path('index4/', views.index4, name='index4'),
	path('index5/', views.index5, name='index5'),
	path('index6/', views.index6, name='index6'),
	path('index7/', views.index7, name='index7'),
	path('index8/', views.index8, name='index8'),
	path('<int:id>', views.flight, name = 'flight'),
	path('index4/<int:id>', views.article_full, name = 'article_full'),

	#re_path(r'^index5/\w+', views.index5),
	

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),

	]
