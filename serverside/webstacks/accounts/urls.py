from django .urls import path
from .views import RegisterView,get_book,create_book,book_details
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView




urlpatterns = [

path('register/',RegisterView.as_view(),name="register"),
path('login/',TokenObtainPairView.as_view(),name="login"),
path('refresh/token/',TokenRefreshView.as_view(),name="refresh"),
path('books/',get_book,name="getBooks"),
path('books/create/',create_book,name="createBooks"),
path('books/<int:pk>/',book_details,name="bookDetail"),
]