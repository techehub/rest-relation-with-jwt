from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import AuthorSerializer, BookSerializer, PublisherSerializer, UserSerializer
from .models import Author,Publisher, Book
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
# Create your views here.

class AuthorView (ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticated,)



class PublisherView (ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    permission_classes = (IsAuthenticated,)


class BookView (ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

