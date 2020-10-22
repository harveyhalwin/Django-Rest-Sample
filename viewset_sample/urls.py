from django.urls import path, include
from .views import StudentView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentView)

urlpatterns = [
    path('', include(router.urls)),
]
