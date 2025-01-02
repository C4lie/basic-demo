from rest_framework import serializers
from .models import Scholarship, Application, Donation


def validate_fund_amount(value):
    if value <= 0:
        raise serializers.ValidationError("Fund amount must be greater than zero.")
    return value

class ScholarshipSerializer(serializers.ModelSerializer):
    fund_amount = serializers.DecimalField(max_digits=10, decimal_places=2, validators=[validate_fund_amount])

    class Meta:
        model = Scholarship
        fields = '__all__'
        
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
