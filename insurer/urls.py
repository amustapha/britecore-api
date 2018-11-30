from django.conf.urls import url

from .views import CreateRisk
urlpatterns = [
    url('^risk/', CreateRisk.as_view())
]