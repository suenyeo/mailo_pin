from django.urls import path

from subscriptionapp.views import SubscriptionRedirectView

app_name = 'subscriptionapp'

urlpatterns=[
    path('subscription/', SubscriptionRedirectView.as_view(),name='subscription')
]