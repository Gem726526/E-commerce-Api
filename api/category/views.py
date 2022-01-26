from rest_framework import viewsets


from .serializer import CategorySerializer
from .models import Category

class CategoryViewset(viewsets.ModelViewSet):
    queryset =  Category.objects.all().order_by('name')
    serializer_class = CategorySerializer