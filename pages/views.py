from django.views.generic import TemplateView
from products.models import Product, Category
from accounts.models import CustomUser


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_featured'] = Product.objects.filter(featured=True).order_by('-created_at')[:12]
        context['products'] = Product.objects.all().order_by('-created_at')[:24]
        context['total_books_count'] = Product.objects.all().count()
        context['total_users_count'] = CustomUser.objects.all().count()
        context['categories_list'] = Category.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
