from django.conf.urls import url, include
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^', include('questionnaire.urls'))
]