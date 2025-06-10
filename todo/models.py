from django.db import models

CHOICES = [
    ('danger', 'Danger'),
    ('high',   'High'),
    ('normal', 'Normal'),
]

class TodoModel(models.Model):
    title    = models.CharField(max_length=100)
    memo     = models.TextField()
    priority = models.CharField(
        max_length=10,          # max_length必須
        choices=CHOICES,        # (actual, human-readable)のタプルリスト
        default='normal'
    )
    date = models.DateField()

    def __str__(self):
        return self.title