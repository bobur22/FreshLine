from rest_framework import permissions

class IsSellerOrReadOnly(permissions.BasePermission):
    """
    Allow sellers to edit their own products.
    Buyers can only read.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.seller == request.user
