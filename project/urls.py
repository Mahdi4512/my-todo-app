from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from app.views import SignUpView

def home_redirect(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', home_redirect),  # صفحه اصلی → لاگین
    path('tasks/', include('app.urls')),  # همه تسک‌ها زیر /tasks/
]
