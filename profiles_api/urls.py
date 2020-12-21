from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


# Assisgn router to a variable
router = DefaultRouter()
# Register specific viewsets with our router
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
