# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Photo

def home(request):
    """
    Se ejecuta en / y carga la plantilla photos/templates/photos/index.html
    :param request: objeto request
    :return: objeto response
    """
    photo_list = Photo.objects.order_by('-created_at')
    context = {
        'photos' : photo_list[:3]
    }
    return render(request, 'photos/index.html', context)