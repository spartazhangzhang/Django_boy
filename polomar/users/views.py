from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from .models import User
# Create your views here.

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # 下面两行来显示根据视图来查找
    slug_field = 'username'
    slug_url_kwarg = 'username'

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ["name"]

    model = User

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username":self.request.user.username})

    def get_object(self):
        #只为发出请求的用户获取用户记录
        return User.objects.get(username=self.request.user.username)

class UserListView(LoginRequiredMixin, ListView):
    model = User
    # #下面两行告诉视图按用户名索引查找
    slug_field = "username"
    slug_url_kwarg = "username"
