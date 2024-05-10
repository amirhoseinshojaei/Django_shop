from rest_framework.permissions import BasePermission

class IsSuperUserOrStaff(BasePermission):

    def has_permission(self, request, view):
        
        if request.user.is_superuser:

            return request.method in ['GET','HEAD','OPTION','PUT','POST','PATCH','DELETE']
        
        if request.user.is_staff:

            return request.method in ['GET']
        
        return False
        