from django.urls.conf import include
from rest_framework import routers
from django.urls import include, path

from backend import views

router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)
router.register(r'blocs', views.BlocViewSet)

urlpatterns = [
    path('', include(router.urls))
]