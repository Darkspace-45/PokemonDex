from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.type}) - Nivel {self.level}"
