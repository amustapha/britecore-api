from django.conf.urls import url

from .views import ListRiskView, RiskDetailView, SubmissionView, ListSubmission

urlpatterns = [
    url('^risks/$', ListRiskView.as_view(), name='risk_list_or_create'),
    url('^risks/(?P<pk>[0-9]+)/$', RiskDetailView.as_view(), name='risk_detail'),
    url('^submit/$', SubmissionView.as_view(), name='risk_form_submission'),
    url('^submissions/(?P<risk>[0-9]+)/$', ListSubmission.as_view(), name='risk_form_submissions'),
]