from django.urls import path,include

from todo.views import TodoList, TodoDetail

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>',TodoDetail.as_view(), name='detail'),
]
