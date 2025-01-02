from django.db import models
from users.models import User

class Scholarship(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    criteria = models.TextField()
    fund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_hash = models.CharField(max_length=255)
    donated_at = models.DateTimeField(auto_now_add=True)
