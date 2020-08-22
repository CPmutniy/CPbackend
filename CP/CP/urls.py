from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from zhkh import views


router = DefaultRouter()

router.register('company', views.CompanyViewSet, basename='company')

urlpatterns = router.urls

urlpatterns.extend([
    path('admin/', admin.site.urls),
])
