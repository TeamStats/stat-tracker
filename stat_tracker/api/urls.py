from django.conf.urls import include, url
from rest_framework import routers

from . import views as api_views


router = routers.DefaultRouter()

router.register(r'activities', api_views.ActivityViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^activities/(?P<pk>\d+)/stat', api_views.StatListCreateView.as_view(), name="create_stat"),
    url(r'^stats/(?P<pk>\d+)', api_views.StatUpdateView.as_view(), name="update_stat"),
]