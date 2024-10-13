# models.py
from django.db import models

class ServiceRequest(models.Model):
    SERVICE_CATEGORIES = [
        ('Gas Delivery and Distribution', 'Gas Delivery and Distribution'),
        ('Customer Service and Billing', 'Customer Service and Billing'),
        ('Safety and Compliance', 'Safety and Compliance'),
        ('Infrastructure Maintenance and Upgrades', 'Infrastructure Maintenance and Upgrades'),
        ('Environmental Stewardship', 'Environmental Stewardship')
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('issue_from_customer', 'Issue from Customer Side')
    ]
    
    service_category = models.CharField(max_length=100, choices=SERVICE_CATEGORIES)
    request_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # New Status Field
