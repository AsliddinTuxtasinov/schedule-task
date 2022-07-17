from django.contrib import admin
from main.models import EmailForTasks, SendMessage


@admin.register(EmailForTasks)
class EmailForTasksAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(SendMessage)
class SendMessageAdmin(admin.ModelAdmin):
    list_display = ['title']
