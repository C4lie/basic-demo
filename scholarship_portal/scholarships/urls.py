from django.urls import path
from .views import ScholarshipListCreateView, ApplicationListCreateView, DonationListCreateView


urlpatterns = [
    path('', ScholarshipListCreateView.as_view(), name='scholarship-list-create'),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('donations/', DonationListCreateView.as_view(), name='donation-list-create'),
]
