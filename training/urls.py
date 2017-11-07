from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'training.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^flow_hosp_live/', include('flow_hosp_live.urls', namespace="flow_hosp_live")),
    url(r'^admin/', include(admin.site.urls)),
]
