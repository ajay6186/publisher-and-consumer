from django.urls import path
from .views import consume_message

urlpatterns = [
    path('consume/', consume_message, name='consume_message'),
]
