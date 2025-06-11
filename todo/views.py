from PIL.ImageFilter import DETAIL
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from todo.models import TodoModel
from django.urls import reverse_lazy

# ? 情報一覧を読み取る
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = '__all__'
    success_url = reverse_lazy('list')  # * データ保存後の遷移先

class TodoDelete(DeleteView):
    model = TodoModel
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
