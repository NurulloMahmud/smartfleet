from rest_framework import permissions


class ManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.department.name == 'management'
