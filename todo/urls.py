from django.urls import path,include

from todo.views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate
urlpatterns = [
    path('', TodoList.as_view(), name='list'),
    path('detail/<int:pk>/',TodoDetail.as_view(), name='detail'),
    path('create/',TodoCreate.as_view(),name='create'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
]
