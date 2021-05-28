from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, DetailView

from accounts.models import CustomUser
from products.models import Product


class LoginSignupView(TemplateView):
    template_name = 'account/signup_login.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Product.objects.filter(owner=self.request.user)
        return context


class ProfileSettingsView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'account/profile_settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_total_books'] = Product.objects.filter(owner=self.request.user).count()
        return context


class AccountDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'account/account_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     print(self.object)
    #     self.object.is_active = False
    #     self.object.save()
    #     response = redirect(reverse_lazy('account_logout'))
    #     response.status_code = 303
    #     return response
