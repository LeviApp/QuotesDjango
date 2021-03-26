from django.urls import path
from quotesbackend.api.views import quotes_api, quote_api

app_name = 'quotesbackend'
urlpatterns = [
    path(f'', quotes_api, name='quotes'),
    path(f'<str:pk>/', quote_api, name='quote'),
]