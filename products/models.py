from django.db import models
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class ProductViews(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ip_address} in Post: {self.product.title}'


class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50,
                              help_text='Derslikler, folklor kitablari ve s. ucun bu hisse bos ola biler',
                              null=True, blank=True
                              )
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/books', default='media/images/book.png')
    price = models.FloatField()
    amount = models.IntegerField(default=1, null=True)
    phone_number = models.CharField(max_length=15)
    additional_contact = models.CharField(max_length=150, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, editable=False, max_length=110)

    @property
    def view_count(self):
        return ProductViews.objects.filter(product=self).count()

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{counter}'
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _("products")
        verbose_name_plural = _("products")
        ordering = ['-created_at']
