from rest_framework import generics
from .models import Scholarship, Application, Donation
from .serializers import ScholarshipSerializer, ApplicationSerializer, DonationSerializer



class ScholarshipListCreateView(generics.ListCreateAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer

class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class DonationListCreateView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
