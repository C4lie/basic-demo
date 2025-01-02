from rest_framework import permissions

class IsStudent(permissions.BasePermission):
    """
    Custom permission to only allow students to view their applications.
    """
    def has_permission(self, request, view):
        return request.user.role == 'student'

class IsDonor(permissions.BasePermission):
    """
    Custom permission to only allow donors to make donations.
    """
    def has_permission(self, request, view):
        return request.user.role == 'donor'

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins to manage scholarships.
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'
