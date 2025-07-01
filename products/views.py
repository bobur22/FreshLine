from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsSellerOrReadOnly

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsSellerOrReadOnly]

class ProductArchiveView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSellerOrReadOnly]

    def patch(self, request, pk):
        product = Product.objects.get(pk=pk)
        self.check_object_permissions(request, product)
        product.status = 'archived'
        product.save()
        return Response({'status': 'archived'}, status=status.HTTP_200_OK)

