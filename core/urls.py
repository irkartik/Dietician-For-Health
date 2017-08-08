from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.homeview, name='home'),

	url(r'^signup$', views.user_signup, name="user_signup"),
    url(r'^login$', views.session_login, name="session_login"),
    url(r'^logout$', views.session_logout, name="session_logout"),

   	url(r'^user/dashboard$', views.user_dashboard, name='user_dashboard'),
    url(r'^user/profile$', views.user_profile, name="user_profile"),
    # url(r'^user/questionnaire$', views.user_questionaire, name="user_questionnaire")

]