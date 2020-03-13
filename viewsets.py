"""
permite el cruce para el drud
"""

from rest_framework import viewsets
from .models import Book
from .serializer import BookSerializer

class BookViewSet(viewsets.ModelViewSet)
    queryset=Book.objects.all()
