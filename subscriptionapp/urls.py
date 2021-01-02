from django.urls import path

from subscriptionapp.views import SubscriptionRedirectView, SubscriptionListView

app_name = 'subscriptionapp'

urlpatterns=[
    path('subscription/', SubscriptionRedirectView.as_view(),name='subscription'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]