from rest_framework import routers
from rest_framework.routers import SimpleRouter

from mainapp.views import TokenViewSet

router = SimpleRouter()

router.register('token', TokenViewSet)

urlpatterns = []

urlpatterns += router.urls