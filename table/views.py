from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from .models import Table
from .serializers import TableSerializer


class TableListCreateAPIView(ListCreateAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class TableDestroyAPIView(DestroyAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    lookup_field = 'pk'


class TableRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    lookup_field = 'pk'