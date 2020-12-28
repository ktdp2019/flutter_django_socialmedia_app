from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url('api_auth/', include('rest_framework.urls')),
    url('', include('apps.account.urls', namespace='account')),
]
