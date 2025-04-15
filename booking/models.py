from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Booking(models.Model):
    STATUS_CHOICES = [
        ('checkedIn', 'CheckedIn'),
        ('pending', 'Pending'),
        ('available', 'Available'),  # available = checkedOut
        ('cancelled', 'Cancelled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey('Workspace', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)  # will be set on checkout
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        ordering = ['-created_at']

    def __str__(self):
        return self.user.email

    def checkout(self):
        """
        Custom method to handle user checkout logic.
        Automatically sets end_time if not already set.
        """
        if self.status != 'available':
            self.status = 'available'
            self.end_time = timezone.now()
            self.save()
