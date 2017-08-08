from django.conf.urls import url
from . import views

app_name = 'questionnaire'

urlpatterns = [
    url(r'^user/questionnaire$', views.questionnaire_new, name='login'),
]