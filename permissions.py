from rest_framework import permissions

class HasPositionPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.position)
