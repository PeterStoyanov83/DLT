# dlt/urls.py
from django.urls import path
from dlt.views import DisplayChainView, ValidateChainView

urlpatterns = [
    path('display_chain/', DisplayChainView.as_view(), name='display_chain'),
    path('validate_chain/', ValidateChainView.as_view(), name='validate_chain'),
    # Other URL patterns for the dlt app
]