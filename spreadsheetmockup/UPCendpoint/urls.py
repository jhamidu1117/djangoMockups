from django.urls import include, path
from rest_framework import routers
from .views import GroupViewSet, UserViewSet, SnippetViewSet, snippet_list, snippet_detail, HandsetViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'snippetset', SnippetViewSet)
router.register(r'Handsets', HandsetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
]