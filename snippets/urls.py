from django.urls import re_path as url, include
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename="user")

# This API URLs are not determined automatically by the router.
# Additionally we include the login URLs for the brawsable API
urlpatterns = [
    url(r'^', include(router.urls))
]