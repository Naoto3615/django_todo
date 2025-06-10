from PIL.ImageFilter import DETAIL
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from todo.models import TodoModel

# ? 情報一覧を読み取る
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

