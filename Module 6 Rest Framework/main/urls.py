from django.urls import path
from .views import BookListView

urlpatterns = [ 
    path('<int:pk>/',BookListView.as_view(), name='employee-detail'),
    path('',BookListView.as_view()),
    
]
