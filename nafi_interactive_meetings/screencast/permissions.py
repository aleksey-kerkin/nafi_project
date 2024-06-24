from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # на время теста чтение разрешено всем пользователям

        return request.user == obj.user or request.user.is_staff
