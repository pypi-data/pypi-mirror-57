import logging
import os
import re

from django.urls import path
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import *

logger = logging.getLogger('django')

urlpatterns = [
    path('index.html', RedirectView.as_view(url='/', permanent=True), name='index.html'),
    path('manifest.json', manifest_json, name='manifest.json'),
    path('service-worker.js', service_worker, name='service-worker'),
    path('precache-manifest.<str:hash>.js', precache_manifest, name='precache-manifest'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/status/', ApiStatusView.as_view(), name='api_status'),
    path('api/chat/<str:room>/', ChatRoomView.as_view(), name='chat_room'),
]


def get_vue_router():
    """Minimal regex router.js parser"""
    r = r'(?<=routes = )(.*)(?=]\n)'
    r_url = r'(?<=path: \')(.*)(?=\',)'
    try:
        with open(
            os.path.join(settings.BASE_DIR, settings.DJANGO_VUE_APP, 'src/router/index.js')
        ) as f:
            router_js = f.read()
        router_data = re.findall(r, router_js, re.DOTALL)
        vue_router = re.findall(r_url, router_data[0])
    except:  # noqa: E722
        # TODO: error handling
        raise
    return vue_router


for route in get_vue_router():
    vue_route = path(route[1:], index_vue, name='vue{0}'.format(route))
    logger.info(f'Vue router: {vue_route}')
    urlpatterns += [vue_route]
