from django.contrib import admin
from .models import Newnote
# Register your models here.

class NewNoteForm(admin.ModelAdmin):
    list_display = ['note_title', 'note_desc', 'user']

admin.site.register(Newnote, NewNoteForm)
