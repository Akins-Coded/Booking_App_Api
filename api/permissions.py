from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Allow access only to users with the 'admin' role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsAdminOrSelf(BasePermission):
    """
    Allow access to admin or to the user modifying their own data.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin' or obj == request.user


class IsEmployee(BasePermission):
    """
    Allow access only to employees.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employee'


class ReadOnly(BasePermission):
    """
    Allow read-only access to anyone.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
