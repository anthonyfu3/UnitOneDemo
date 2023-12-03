from django import forms
from .models import AircraftNote

class NoteForm(forms.ModelForm):
    class Meta:
        model = AircraftNote
        fields = '__all__'
        widgets = {
            'service_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'eta': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'etd': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            "created_at": forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class EditNoteForm(forms.ModelForm):
    class Meta:
        model = AircraftNote
        fields = '__all__'
        widgets = {
            'service_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'eta': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'etd': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            "created_at": forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }