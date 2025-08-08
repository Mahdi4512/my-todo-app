from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from .models import Task
# ثبت‌نام
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name ='registration/signup.html'
    success_url = reverse_lazy('login')

# فقط تسک‌های کاربر جاری را نشان بده
class Tasklist(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-id')

class Taskdetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

class Tasknew(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class Taskupdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

class Taskdelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

class CompleteTaskView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, owner=request.user)
        task.is_completed = True
        task.save()
        return redirect('task_list')
