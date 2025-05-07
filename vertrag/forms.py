from django import forms
from .models import *

class FirmaForm(forms.ModelForm):
    class Meta:
        model = Firma
        fields = '__all__'

class StaneortForm(forms.ModelForm):
    class Meta:
        model = Standort
        fields = ['bezeichnung']  

class TaetigkeitForm(forms.ModelForm):
    class Meta:
        model = Taetigkeit
        fields = ['bezeichnung']

class VertragsartForm(forms.ModelForm):
    class Meta:
        model = Vertragsart
        fields = ['bezeichnung']

class LohnartForm(forms.ModelForm):
    class Meta:
        model = Lohnart
        fields = ['bezeichnung']

class VertragForm(forms.ModelForm):
    class Meta:
        model = Vertrag
        fields = '__all__'  # Alle Felder im Formular anzeigen
        widgets = {
            'beginn': forms.DateInput(attrs={'type': 'date'}),
        }