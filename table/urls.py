from django.urls import path
from .views import TableListCreateAPIView, TableDestroyAPIView, TableRetrieveUpdateAPIView

urlpatterns = [
    path('table-list-or-create', TableListCreateAPIView.as_view()),
    path('table-destroy/<int:pk>', TableDestroyAPIView.as_view()),
    path('table/<int:pk>', TableRetrieveUpdateAPIView.as_view()),
]
