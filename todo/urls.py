from django.urls import path
from todo.views import create_todo, index, todos

urlpatterns = [
	path('', todos),
	path('index/', index),
	path('create_todo/', create_todo, name="create"),
]