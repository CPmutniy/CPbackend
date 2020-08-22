from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from zhkh import views


router = DefaultRouter()

router.register('company', views.CompanyViewSet, basename='company')
router.register('adress', views.AdressViewSet, basename='adress')
router.register('person', views.PersonViewSet, basename='person')
router.register('voting', views.VotingViewSet, basename='voting')
router.register('question', views.QuestionViewSet, basename='question')
router.register('answer', views.AnswerViewSet, basename='answer')

urlpatterns = router.urls

urlpatterns.append(path('admin/', admin.site.urls))
