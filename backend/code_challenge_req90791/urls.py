from django.urls import include, path
from rest_framework import routers
from echocatch_tours_kanban import views

router = routers.DefaultRouter()
router.register('swimlanes', views.SwimlaneViewSet)
router.register('boats', views.BoatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
