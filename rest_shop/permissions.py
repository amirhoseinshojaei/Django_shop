from rest_framework.permissions import BasePermission


class IsUperUserOrStaff(BasePermission):

    """
    Custom permission to allow super user full access but staff user safe method access
    """

    def has_permission(self, request, view):
        
        if request.user.is_superuser:

            return request.method in ['GET','HEAD','OPTION','PUT','POST','PATCH','DELETE']
        
        if request.user.is_staff:

            return request.method in ['GET','HEAD','OPTION']
        
        return False