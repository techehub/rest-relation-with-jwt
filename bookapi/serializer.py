from rest_framework import serializers
from .models import Book, Publisher, Author
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):

   class Meta:
       model = Book
       fields = '__all__'



class PublisherSerializer(serializers.ModelSerializer):

   class Meta:
       model = Publisher
       fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

   class Meta:
       model = Author
       fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user