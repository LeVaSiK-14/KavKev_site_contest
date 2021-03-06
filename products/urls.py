from rest_framework.routers import SimpleRouter
from django.urls import path

from products.views import (
    CategoryViewSet,
    ProductsViewSet,
    CartViewSet,
    RegistrationAPIView,
    AuthenticationAPIView)

router = SimpleRouter()

router.register('category', CategoryViewSet)
router.register('product', ProductsViewSet)
router.register('my_cart', CartViewSet)


urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', AuthenticationAPIView.as_view()),
]

urlpatterns += router.urls
