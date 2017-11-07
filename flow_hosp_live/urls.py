from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.index, name="index"),
	url(r'^login/$', views.login, name="login"),
	url(r'^login_check/$', views.login_check, name="login_check"),
	url(r'^dashboard/(?P<trainee_id>[0-9]+)/$', views.dashboard, name="dashboard"),
	url(r'^company/(?P<trainee_id>[0-9]+)/$', views.company, name="company"),
	url(r'^external_training/(?P<trainee_id>[0-9]+)/$', views.external_training, name="external_training"),

]