from rest_framework import routers, permissions
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
router.register(r'stats', views.StatViewSet)
router.register(r'cardstats', views.CardStatViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Enlightened Pitch API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]