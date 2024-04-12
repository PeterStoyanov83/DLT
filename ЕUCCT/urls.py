
from django.urls import path
from dlt.views import DisplayChainView, ValidateChainView, DisplayTransactionsView

urlpatterns = [
    path('display_chain/', DisplayChainView.as_view(), name='display_chain'),
    path('validate_chain/', ValidateChainView.as_view(), name='validate_chain'),
    path('transactions/', DisplayTransactionsView.as_view(), name='transactions')
    # Other URL patterns for the dlt app
]