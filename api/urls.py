from django.urls import include, path

from .views import schema_view

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('accounts/', include('api.accounts.urls')),
    path('products/', include('api.products.urls')),
    path('contact/', include('api.contact.urls')),
]
