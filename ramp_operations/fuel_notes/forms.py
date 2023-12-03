from django import forms
from .models import AircraftNote

class NoteForm(forms.ModelForm):
    class Meta:
        model = AircraftNote
        fields = '__all__'  # Or list specific fields you want in your form
