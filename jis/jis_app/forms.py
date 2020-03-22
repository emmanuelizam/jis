from django import forms
from .models import Case, CaseAdjournment, CaseProceeding

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['case_identification_number', 'defendant_name', 'defendant_address', 'crime_type', 'crime_location', 'name_of_arresting_officer', 'date_committed', 'time_committed', 'date_of_arrest', 'time_of_arrest', 'public_prosecutor', 'presiding_judge', 'date_of_first_hearing', 'time_of_first_hearing', 'date_of_completion_of_hearing', 'time_of_completion_of_hearing', 'summary_of_judgement', 'case_is_closed']
        widgets = {
            'date_committed': DateInput(),
            'time_committed': TimeInput(),
            'date_of_arrest': DateInput(),
            'time_of_arrest': TimeInput(),
            'date_of_first_hearing': DateInput(),
            'time_of_first_hearing': TimeInput(),
            'date_of_completion_of_hearing': DateInput(),
            'time_of_completion_of_hearing': TimeInput()
        }

class CaseProceedingForm(forms.ModelForm):
    class Meta:
        model = CaseProceeding
        fields = '__all__'
        widgets = {
            'date_of_proceeding': DateInput(),
            'time_of_proceeding': TimeInput(),
            'date_of_next_proceeding': DateInput(),
            'time_of_next_proceeding': TimeInput(),
        }

class CaseAdjournmentForm(forms.ModelForm):
    class Meta:
        model = CaseAdjournment
        fields = '__all__'
        widgets = {
            'date_adjourned_to': DateInput(),
            'time_adjourned_to': TimeInput(),
        }
