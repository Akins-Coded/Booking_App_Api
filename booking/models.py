from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organisation(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Hub(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='hubs')

    def __str__(self):
        return self.name


class WorkspaceType(models.TextChoices):
    PERSONAL = 'personal', 'Personal'
    CONFERENCE = 'conference', 'Conference Room'
    TEAM = 'team', 'Team'
    OTHER = 'other', 'Other'


class WorkspaceStatus(models.TextChoices):
    CHECKED_IN = 'checkedin', 'Checked In'
    AVAILABLE = 'available', 'Available'
    BOOKED = 'booked', 'Booked'
    MAINTENANCE = 'maintenance', 'Maintenance'


class Workspace(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE, related_name='workspaces')
    type = models.CharField(max_length=20, choices=WorkspaceType.choices)
    status = models.CharField(max_length=20, choices=WorkspaceStatus.choices)

    def __str__(self):
        return f"{self.type} workspace in {self.hub.name}"


class BookingStatus(models.TextChoices):
    CHECKED_IN = 'checkedIn', 'Checked In'
    PENDING = 'pending', 'Pending'
    AVAILABLE = 'available', 'Checked Out'
    CANCELLED = 'cancelled', 'Cancelled'


class Booking(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=BookingStatus.choices)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.status}"

    def checkout(self):
        """Set end_time and status when checking out."""
        if self.status != BookingStatus.AVAILABLE:
            self.status = BookingStatus.AVAILABLE
            self.end_time = timezone.now()
            self.save()
