from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


# class APIKeyPermission(permissions.BasePermission):
#     message = 'Adding customers not allowed.'
#
#     def has_permission(self, request, view):
#         api_key = request.GET.get('api_key')
#         return api_key == "api_key"
