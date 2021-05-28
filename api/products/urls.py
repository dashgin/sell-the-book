from django.urls import path
from .views import (ProductListCreateAPIView,
                    ProductByUserListAPIView,
                    ProductRetrieveDestroyAPIView,
                    ProductsByCategoryListAPIView,
                    CategoryListAPIView,
                    )

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<slug:slug>/', ProductRetrieveDestroyAPIView.as_view()),
    path('<int:user_id>/products/', ProductByUserListAPIView.as_view()),

    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<slug:category_slug>/', ProductsByCategoryListAPIView.as_view()),

]