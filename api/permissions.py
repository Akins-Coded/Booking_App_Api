from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Allows access only to users with 'admin' role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsManager(BasePermission):
    """
    Allows access only to users with 'manager' role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'


class IsMember(BasePermission):
    """
    Allows access only to users with 'member' role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'member'

class IsAdminOrSelf(BasePermission):
    """
    Allows access if the user is an admin or accessing their own object.
    Assumes the view has a `get_object()` method returning the target user object.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            request.user.role == 'admin' or obj == request.user
        )


class IsAdminOrManager(BasePermission):
    """
    Allows access to users with either 'admin' or 'manager' roles.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'manager']


class IsReadOnly(BasePermission):
    """
    Allows only safe (read-only) methods like GET, HEAD, OPTIONS.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
