
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Book




User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password':{"write_only":True}}


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'




