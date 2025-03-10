from django.db import models
from jobs.models import Job  # Assuming Job model is in jobs.models

class Proposal(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='proposals')
    freelancer_name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    submitted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Proposal for {self.job.title} by {self.freelancer_name}'
