from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'lesson_watch_stats', views.LessonWatchStatsViewSet, basename='user')
router.register(r'product_stats', views.ProductStatsViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]


