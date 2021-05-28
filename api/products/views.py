from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

from products.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from api.permissions import IsOwnerOrReadOnly


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'price', 'author']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'slug'


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


class ProductsByCategoryListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs['category_slug']
        queryset = Product.objects.filter(category__slug=slug)
        return queryset


class ProductByUserListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.kwargs['user_id']
        queryset = Product.objects.filter(owner_id=pk)
        return queryset
