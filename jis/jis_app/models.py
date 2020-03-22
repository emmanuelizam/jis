from django.db import models
from django.urls import reverse

# Create your models here.
class Case(models.Model):
    case_identification_number = models.BigAutoField(primary_key=True)
    defendant_name = models.CharField(blank=True, max_length=500)
    defendant_address = models.CharField(blank=True, max_length=500)
    crime_type = models.CharField(blank=True, max_length=500)
    date_committed = models.DateField(blank=True)
    time_committed = models.TimeField(blank=True)
    crime_location = models.CharField(blank=True, max_length=500)
    name_of_arresting_officer = models.CharField(blank=True, max_length=500)
    date_of_arrest = models.DateField(blank=True)
    time_of_arrest = models.TimeField(blank=True)
    date_of_first_hearing = models.DateField(blank=True)
    time_of_first_hearing = models.TimeField(blank=True)
    date_of_completion_of_hearing = models.DateField(blank=True)
    time_of_completion_of_hearing = models.TimeField(blank=True)
    public_prosecutor = models.CharField(blank=True, max_length=500)
    presiding_judge = models.CharField(blank=True, max_length=500)
    summary_of_judgement = models.TextField(blank=True)
    case_is_closed = models.BooleanField(blank=True, default=False)

    def get_absolute_url(self):
        return reverse('case_create_form')

class CaseProceeding(models.Model):
    proceeding = models.TextField(blank=True)
    date_of_proceeding = models.DateField(blank=True)
    time_of_proceeding = models.TimeField(blank=True)
    date_of_next_proceeding = models.DateField(blank=True)
    time_of_next_proceeding = models.TimeField(blank=True)
    case = models.ForeignKey(to=Case, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('case_proceeding_create_form')

class CaseAdjournment(models.Model):
    reason = models.TextField(blank=True)
    date_adjourned_to = models.DateField(blank=True)
    time_adjourned_to = models.TimeField(blank=True)
    case = models.ForeignKey(to=Case, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('case_adjournment_create_form')