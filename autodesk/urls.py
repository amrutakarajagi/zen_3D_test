from django.urls import path

from . import views

urlpatterns = [
	path('', views.viewer, name='viewer'),
	path('token/', views.generate_token, name='generate_token'),
]