from django.conf.urls import url

from .views import ListRiskView, RiskDetailView

urlpatterns = [
    url('^risks/$', ListRiskView.as_view()),
    url('^risks/(?P<pk>[0-9]+)/$', RiskDetailView.as_view())
]