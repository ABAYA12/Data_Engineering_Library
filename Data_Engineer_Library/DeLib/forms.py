from django import forms
from .models import PipelineDetails

class PipelineDetailsForm(forms.ModelForm):
    class Meta:
        model = PipelineDetails
        fields = '__all__'
