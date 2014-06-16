# -*- coding: utf-8 -*-
from rest_framework import permissions


class PhotoPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Permite realizar cualquier operacion sobre las fotos
        :param request: objeto request
        :param view: vista desde donde se ejecuta la acción
        :return: boolean
        """
        return True


    def has_object_permission(self, request, view, obj):
        """
        Define si se tiene permiso para hacer GET, PUT o DELETE
        sobre una foto.
        Sólo tiene permiso si es propietario o es superuser
        :param request: objeto request
        :param view: vista desde donde se ejecuta
        :param obj: objeto sobre el que se ejecuta
        :return: boolean
        """
        if request.user.is_superuser or obj.owner == request.user:
            return True
        else:
            return False