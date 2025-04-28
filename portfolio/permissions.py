# backend/portfolio/permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Allow anyone to read (GET, HEAD, OPTIONS),
    but only allow edits if the object belongs to request.user.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed
        if request.method in SAFE_METHODS:
            return True
        # Write permissions only to the owner of the portfolio
        return obj.portfolio.user == request.user
