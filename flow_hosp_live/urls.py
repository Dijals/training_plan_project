from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.index, name="index"),
	url(r'^login/$', views.login, name="login"),
	url(r'^login_check/$', views.login_check, name="login_check"),
	url(r'^user_account/(?P<trainee_id>[0-9]+)/$', views.user_account, name="user_account"),

]