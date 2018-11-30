from django.conf.urls import url

from .views import ListRiskView, RiskDetailView

urlpatterns = [
    url('^risk/$', ListRiskView.as_view()),
    url('^risk/(?P<pk>[0-9]+)/$', RiskDetailView.as_view())
]