from django.contrib import admin

from api.models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('datum', 'names', 'cell', 'question1', 'question2', 'temperature')
    readonly_fields = ('datum',)