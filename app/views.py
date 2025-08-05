from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from .models import Task
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, redirect
class Tasklist(ListView):
    model=Task
    template_name='task_list.html'

class Taskdetail(DetailView):
    model=Task
    template_name='task_detail.html'

class Tasknew(CreateView):
    model = Task
    fields = ['title', 'description']  # created_at اتومات هست
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

class Taskupdate(UpdateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
class Taskdelete(DeleteView):
    model=Task
    template_name='task_delete.html'
    success_url=reverse_lazy('task_list')
class CompleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = True
        task.save()
        return redirect('task_list')

