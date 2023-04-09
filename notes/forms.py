from django import forms
from . import models

class NotesForm(forms.ModelForm):
    class Meta:
        model = models.Newnote
        fields = ['note_title', 'note_desc', 'user']