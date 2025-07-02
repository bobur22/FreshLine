from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsBuyerOrAdmin

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Order.objects.all()
        return Order.objects.filter(buyer=user)

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        total_price = product.price * quantity
        serializer.save(buyer=self.request.user, total_price=total_price)

class OrderRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBuyerOrAdmin]

    def perform_update(self, serializer):
        # Only admin or seller should change status
        user = self.request.user
        if 'status' in serializer.validated_data:
            if user.role not in ['admin', 'seller']:
                raise serializers.ValidationError("You are not allowed to change status.")
        serializer.save()
