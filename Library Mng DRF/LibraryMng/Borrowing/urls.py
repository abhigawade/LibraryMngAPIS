from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BorrowModelView


router = DefaultRouter()
router.register(r'', BorrowModelView, basename='borrow')

urlpatterns = [
    path('', include(router.urls)),
]