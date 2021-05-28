from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAdminUser, AllowAny

# Swagger view
schema_view = get_schema_view(
    openapi.Info(
        title="STB API",
        default_version='v1',
        description="Book",
        contact=openapi.Contact(email="contact@stb.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)
