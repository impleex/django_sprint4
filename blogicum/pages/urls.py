from django.urls import path
from django.views.generic import TemplateView

app_name = 'pages'

urlpatterns = [
    path(
        'faq/',
        TemplateView.as_view(template_name='pages/faq.html'),
        name='faq'
    ),
    path(
        'support/',
        TemplateView.as_view(template_name='pages/support.html'),
        name='support'
    ),
    path(
        'about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'
    ),
    path(
        'rules/',
        TemplateView.as_view(template_name='pages/rules.html'),
        name='rules'
    ),
]
