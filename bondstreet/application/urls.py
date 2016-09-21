from django.conf.urls import url

from . import views
from . import forms

urlpatterns = [
    url(r'^$', views.ApplicationWizard.as_view(
        [forms.ApplicationForm1,
         forms.ApplicationForm2,
         forms.ApplicationForm3,
         forms.ApplicationForm4,
         forms.ApplicationForm5])),
]
