from functools import partial
from django.urls import path
from mainapp.views import ListCreateToken, RetrieveUpdateToken

urlpatterns = [
    path('token/', ListCreateToken.as_view()),
    path('token/<slug:slug>/', RetrieveUpdateToken.as_view()),
]
