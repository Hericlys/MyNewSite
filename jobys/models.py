from django.db import models


class Joby(models.Model):
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobys'

    # customer
    customer_first_name = models.CharField(max_length=30)
    customer_last_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.EmailField()

    # Project
    project_type = models.CharField(max_length=80)
    project_description = models.TextField(max_length=2000)
    project_date_request = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("requested", "requested"),
        ("sent", "sent"),
        ("In-production", "In-production"),
        ("Finished", "Finished"),
        ("discontinued", "discontinued"),
    ]
    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default=STATUS_CHOICES[0]
    )
    service_contract = models.FileField(
        upload_to="service_contract/%M/",
        null=True, blank=True, default=""
    )
