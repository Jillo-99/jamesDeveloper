from  rest_framework import generics
from django.contrib.auth.models import User
from .serializer import UserSerializer,BookSerializer
from rest_framework.decorators import api_view
from .models import Book
from rest_framework .response import Response
from rest_framework import status




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def get_book(request):
    books = Book.objects.all()
    serializerData = BookSerializer(books,many=True).data
    return Response(serializerData)


@api_view(['POST'])
def create_book(request):
    data = request.data
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE','PUT'])
def book_details(request,pk):


    try:
        book = Book.objects.get(pk=pk)


    except Book.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_301_MOVED_PERMANENTLY)
    elif request.method == 'PUT':
        data = request.data
        serializer = BookSerializer(book,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
   


