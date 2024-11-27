from rest_framework.permissions import BasePermission

class IsMangaCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.creator == request.user