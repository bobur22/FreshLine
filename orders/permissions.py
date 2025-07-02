from rest_framework import permissions

class IsBuyerOrAdmin(permissions.BasePermission):
    """
    Allow buyers to manage their own orders.
    Admins can manage all.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        return obj.buyer == request.user
