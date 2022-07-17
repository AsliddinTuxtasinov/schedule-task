from django.db import models


class EmailForTasks(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class SendMessage(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    emails = models.ManyToManyField(to=EmailForTasks, related_name="send_message")
    send_at = models.DateTimeField()

    def __str__(self):
        return self.title
