from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Book API. Visit /api/books/ for the API.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('', home, name='home'),  # Add this line for root URL
]