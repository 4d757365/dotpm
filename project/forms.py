from django.forms import ModelForm
from .models import ProjectFile
from django import forms

class ProjectFileForm(ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['name', 'attachment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-6 px-6 bg-slate-400 rounded-lg text-white outline-none'}),
            'attachment': forms.FileInput(attrs={'class': 'w-full py-6 px-6',}),
        }
        