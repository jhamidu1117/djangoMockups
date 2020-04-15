from django.urls import include, path
from rest_framework import routers
from .views import GroupViewSet, UserViewSet, snippet_list, snippet_detail


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
]