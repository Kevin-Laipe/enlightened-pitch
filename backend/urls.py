from django.urls.conf import include
from rest_framework import routers
from django.urls import include, path

from backend import views

router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)
router.register(r'blocs', views.BlocViewSet)
router.register(r'classes', views.ClassViewSet)
router.register(r'types', views.TypeViewSet)
router.register(r'talents', views.TalentViewSet)
router.register(r'keywords', views.KeywordViewSet)
router.register(r'relesenotes', views.ReleasenoteViewSet)
router.register(r'subtypes', views.SubtypeViewSet)

urlpatterns = [
    path('', include(router.urls))
]