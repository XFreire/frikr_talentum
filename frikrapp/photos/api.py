# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from serializers import UserSerializer, PhotoSerializer, PhotoListSerializer, FileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from models import Photo, VISIBILITY_PUBLIC, File
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from permissions import PhotoPermission
from django.db.models import Q
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context, loader
from django.utils.html import strip_tags


WELCOME_EMAIL_TEMPLATE = getattr(settings, 'WELCOME_EMAIL_TEMPLATE', 'photos/email/welcome.html')
WELCOME_EMAIL_SUBJECT = 'Hola {0} {1}!'
WELCOME_EMAIL_FROM = 'root@localhost'
DEBUG = getattr(settings, 'DEBUG', False)

class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = UserSerializer(data=request.DATA) # en lugar request.POST
        if serializer.is_valid():
            new_user = serializer.save()
            self.send_welcome_email(new_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def send_welcome_email(self, user):
        # recogemos el asunto, direccion remitente y destino
        subject = WELCOME_EMAIL_SUBJECT.format(user.first_name, user.last_name)
        from_email = WELCOME_EMAIL_FROM
        to = user.email

        # Renderizamos la plantilla con el e-mail de bienvenida
        template = loader.get_template(WELCOME_EMAIL_TEMPLATE)
        context = Context( { 'new_user': user } )
        html_content = template.render(context) # renderizamos la plantilla
        text_content = strip_tags(html_content) # texto plano sin HTML

        # creamos un mensaje de e-mail
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=(not DEBUG)) # si falla el envío de e-mail, no peta



class UserDetailAPI(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user == user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user == user:
            serializer = UserSerializer(user, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if request.user.is_superuser or request.user == user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



class PhotoAPIQueryset:


    def get_queryset(self):
        """
        Devuelve un queryset en función de varios criterios
        """
        if self.request.user.is_superuser:
            return Photo.objects.all()
        elif self.request.user.is_authenticated():
            return Photo.objects.filter(Q(visibility=VISIBILITY_PUBLIC) | Q(owner=self.request.user))
        else:
            return Photo.objects.filter(visibility=VISIBILITY_PUBLIC)




class PhotoListAPI(PhotoAPIQueryset, ListCreateAPIView):
    """
    Implementa el API de listado (GET) y creación (POST) de fotos
    (Sí, en serio)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, PhotoPermission)



    def get_serializer_class(self):
        if self.request.method == "POST":
            return PhotoSerializer
        else:
            return self.serializer_class
        #return PhotoSerializer if self.request.method == "POST" else self.serializer_class



    def pre_save(self, obj):
        """
        Asigna la autoría de la foto al usuario autenticado al crearla
        """
        obj.owner = self.request.user


class PhotoDetailAPI(PhotoAPIQueryset, RetrieveUpdateDestroyAPIView):
    """
    Implementa el API de detalle (GET), actualización (PUT), y borrado (DELETE)
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, PhotoPermission)



class PhotoUploadAPI(CreateAPIView):
    """
    Permite subir fotos
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsAuthenticated,)





















