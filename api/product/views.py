
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product



class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all().order_by('name')
        serializer_class = ProductSerializer

# class AddProductView(APIView):
#     def post(self, request):
#         data =  request.data
#         serializer_class = ProductSerializer(data)
#         serializer_class.is_valid()
#         serializer_class.save()
#         return Response({'message':'sucessfully added'})
